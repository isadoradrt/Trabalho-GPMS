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