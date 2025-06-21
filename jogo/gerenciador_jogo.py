from jogador import Jogador
from doenca import Doenca
from baralho import Baralho
from baralho_infeccao import BaralhoInfeccao
from cartas import CartaCidade

class GerenciadorJogo:
    def __init__(self):
        self.jogadores = []
        self.doencas = []
        self.baralho_jogador = Baralho()
        self.baralho_infeccao = BaralhoInfeccao()
        self.cidades = []  # Lista de objetos CartaCidade
        self.jogador_atual = None
        self.turno = 0

    def adicionar_jogador(self, jogador):
        self.jogadores.append(jogador)
        if not self.jogador_atual:
            self.jogador_atual = jogador

    def adicionar_doenca(self, doenca):
        self.doencas.append(doenca)

    def proximo_turno(self):
        self.turno += 1
        index = self.turno % len(self.jogadores)
        self.jogador_atual = self.jogadores[index]
        print(f"Turno {self.turno}: vez de {self.jogador_atual.nome}")

    def inicializar_cidades(self, cidades):
        self.cidades = cidades

    def exibir_estado(self):
        print(f"Turno: {self.turno}")
        for jogador in self.jogadores:
            print(jogador)
        for doenca in self.doencas:
            print(doenca)
