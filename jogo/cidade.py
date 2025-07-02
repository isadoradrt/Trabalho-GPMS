from jogo.constantes import CIDADES
from jogo.constantes import CORES_DOENCAS

class Cidade:
    def __init__(self, nome: str, cor: str, posicao: tuple = (0, 0)):
        self.nome = nome
        self.cor = cor
        self.conexoes = []
        self.cubos_doenca = {"laranja": 0, "verde": 0, "roxo": 0}
        self.posicao = posicao

    def conectar(self, outra_cidade):
        if outra_cidade not in self.conexoes:
            self.conexoes.append(outra_cidade)
            outra_cidade.conexoes.append(self)

    def adicionar_cubo(self, cor):
        if cor in self.cubos_doenca:
            self.cubos_doenca[cor] += 1

    def remover_cubos(self, cor, quantidade=1):
        if cor in self.cubos_doenca:
            self.cubos_doenca[cor] = max(0, self.cubos_doenca[cor] - quantidade)

