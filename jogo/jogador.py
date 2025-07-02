from jogo.cartas import Carta
from jogo.constantes import MAX_CARTAS_MAO

class Jogador:
    def __init__(self, nome, personagem, cidade_inicial, cartas=None):
        self.nome = nome
        self.personagem = personagem  
        self.cidade_atual = cidade_inicial  
        self.cartas = cartas or []  
        self.acoes_restantes = 4
        self.estacoes_pesquisa = []

    def mover_para(self, nova_cidade):
        if nova_cidade in self.cidade_atual.conexoes:
            self.cidade_atual = nova_cidade
            self.acoes_restantes -= 1
            print(f"{self.nome} moveu-se para {nova_cidade.nome}")
        else:
            print("Cidade não conectada.")

    def tratar_doenca(self, cor=None):
        if cor is None and self.cidade_atual.cubos_doenca:
            cor = max(self.cidade_atual.cubos_doenca, key=lambda c: self.cidade_atual.cubos_doenca[c])

        if cor and self.cidade_atual.cubos_doenca.get(cor, 0) > 0:
            if self.personagem == "Hornet":
                self.cidade_atual.cubos_doenca[cor] = 0  
            else:
                self.cidade_atual.cubos_doenca[cor] -= 1
            self.acoes_restantes -= 1
            print(f"{self.nome} tratou {cor} em {self.cidade_atual.nome}")
        else:
            print("Não há doença dessa cor para tratar.")

    def descobrir_cura(self, cor_doenca, doenca):
        cartas_da_cor = [c for c in self.cartas if c.cor == cor_doenca]
        exigencia = 3 if self.personagem == "Monomon" else 5

        if len(cartas_da_cor) >= exigencia:
            for c in cartas_da_cor[:exigencia]:
                self.cartas.remove(c)
            self.acoes_restantes -= 1
            doenca.curar()
            print(f"{self.nome} descobriu a cura para {cor_doenca}")
            return True
        else:
            print("Cartas insuficientes para descobrir cura.")
            return False

    def compartilhar_carta(self, outro_jogador, carta):
        mesma_cidade = self.cidade_atual == outro_jogador.cidade_atual
        if carta in self.cartas and (mesma_cidade or self.personagem == "Cornifer"):
            self.cartas.remove(carta)
            outro_jogador.cartas.append(carta)
            self.acoes_restantes -= 1
            print(f"{self.nome} compartilhou a carta {carta.nome}")
        else:
            print("Condições para compartilhar carta não atendidas.")

    def construir_estacao(self):
        if self.cidade_atual not in self.estacoes_pesquisa:
            self.estacoes_pesquisa.append(self.cidade_atual)
            self.acoes_restantes -= 1
            print(f"{self.nome} construiu estação em {self.cidade_atual.nome}")
        else:
            print("Esta cidade já tem uma estação.")

    def usar_acao_especial(self, outro_jogador):
        if self.personagem == "Grimm":
            print(f"{self.nome} pode mover {outro_jogador.nome} como se fosse ele.")

    def adicionar_carta_mao(self, carta):
        if len(self.cartas) < MAX_CARTAS_MAO:
            self.cartas.append(carta)
            print(f"{self.nome} pegou a carta {carta.nome}")
        else:
            print(f"{self.nome} já está com {MAX_CARTAS_MAO} cartas na mão!")

    def remover_carta_mao(self, carta):
        if carta in self.cartas:
            self.cartas.remove(carta)
            print(f"{self.nome} descartou a carta {carta.nome}")

    def resetar_acoes(self):
        self.acoes_restantes = 4

    def __str__(self):
        return f"{self.nome} ({self.personagem}) - {self.cidade_atual.nome}"
