from jogo.jogador import Jogador
from jogo.doenca import Doenca
from jogo.baralho import Baralho
from jogo.baralho_infeccao import BaralhoInfeccao
from jogo.cartas import TipoCarta
from jogo.constantes import CORES_DOENCA, MAX_CUBOS_POR_COR, MAX_SURTOS


class GerenciadorJogo:
    def __init__(self):
        self.jogadores = []
        self.doencas = {cor: Doenca(cor) for cor in CORES_DOENCA}
        self.baralho_jogador = Baralho()
        self.baralho_infeccao = BaralhoInfeccao()
        self.cidades = {}  # nome -> Cidade
        self.jogador_atual = None
        self.turno = 0
        self.nivel_infeccao = 2
        self.surtos = 0
        self.descarte_infeccao = []

    def adicionar_jogador(self, jogador):
        self.jogadores.append(jogador)
        if not self.jogador_atual:
            self.jogador_atual = jogador

    def inicializar_cidades(self, cidades):
        self.cidades = cidades

    def proximo_turno(self):
        self.turno += 1
        index = self.turno % len(self.jogadores)
        self.jogador_atual = self.jogadores[index]
        self.jogador_atual.resetar_acoes()
        print(f"Turno {self.turno}: vez de {self.jogador_atual.nome}")

    def executar_turno(self):
        jogador = self.jogador_atual
        print(f"Ações restantes de {jogador.nome}: {jogador.acoes_restantes}")
        self.comprar_cartas(jogador)
        self.infectar_cidades()
        self.verificar_derrota()
        self.verificar_vitoria()
        self.proximo_turno()

    def comprar_cartas(self, jogador):
        for _ in range(2):
            carta = self.baralho_jogador.comprar()
            if carta is None:
                print("Baralho de jogador esgotado! Derrota!")
                exit()
            if carta.tipo == TipoCarta.EPIDEMIA:
                print("EPIDEMIA!")
                self.tratar_epidemia()
            else:
                jogador.adicionar_carta_mao(carta)

    def tratar_epidemia(self):
        self.nivel_infeccao = min(4, self.nivel_infeccao + 1)
        carta = self.baralho_infeccao.pegar_carta_base()
        if not carta:
            return
        cidade = self.cidades[carta.nome]
        self.infectar(cidade, carta.cor, 3)
        self.baralho_infeccao.reciclar_descarte(self.descarte_infeccao)
        self.descarte_infeccao = []

    def infectar_cidades(self):
        for _ in range(self.nivel_infeccao):
            carta = self.baralho_infeccao.comprar()
            if carta is None:
                continue
            cidade = self.cidades[carta.nome]
            self.infectar(cidade, carta.cor)
            self.descarte_infeccao.append(carta)

    def infectar(self, cidade, cor, quantidade=1):
        if self.doencas[cor].curada:
            print(f"{cor} já foi curada. Nenhuma infecção em {cidade.nome}.")
            return

        if cidade.cubos_doenca[cor] + quantidade > 3:
            self.tratar_surtos(cidade, cor)
        else:
            cidade.cubos_doenca[cor] += quantidade
            print(f"{cidade.nome} recebeu {quantidade} cubo(s) de {cor}")


    def tratar_surtos(self, cidade, cor):
        if cidade.cubos_doenca[cor] >= 3:
            print(f"SURTO em {cidade.nome}!")
            self.surtos += 1
            for vizinha in cidade.conexoes:
                if vizinha.cubos_doenca[cor] < 3:
                    vizinha.cubos_doenca[cor] += 1
        if self.surtos >= MAX_SURTOS:
            print(f"{MAX_SURTOS} surtos atingidos. Derrota!")
            exit()

    def verificar_derrota(self):
        for cor in self.doencas:
            total = sum([c.cubos_doenca[cor] for c in self.cidades.values()])
            if total > MAX_CUBOS_POR_COR:
                print(f"Esgotaram-se os cubos da doença {cor}. Derrota!")
                exit()

    def verificar_vitoria(self):
        if all(doenca.curada for doenca in self.doencas.values()):
            print("Todas as doenças foram curadas. Vitória!")
            exit()

    def exibir_estado(self):
        print(f"Turno: {self.turno} | Surtos: {self.surtos} | Nível de infecção: {self.nivel_infeccao}")
        for jogador in self.jogadores:
            print(jogador)
        for doenca in self.doencas.values():
            print(doenca)