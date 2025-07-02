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

POSICOES_CIDADES = {
    # Laranja
    "Penhascos Uivantes": (100, 100),
    "Dirtmouth": (300, 100),
    "Pico de Cristal": (500, 100),
    "Encruzilhada Esquecida": (400, 250),
    "Cidade das Lágrimas": (600, 300),
    "Terra do Descanso": (700, 150),

    # Verde
    "Caminho Verde": (100, 350),
    "Jardins da Rainha": (100, 500),
    "Cânion da Névoa": (200, 400),
    "Ermos Fúngicos": (400, 450),
    "Hidrovia Real": (500, 600),
    "Vila dos Louva-a-Deus": (300, 650),

    # Roxo
    "Ninho Profundo": (100, 750),
    "Bacia Antiga": (500, 750),
    "Borda do Reino": (800, 300),
    "A Colmeia": (700, 600),
    "Coliseu dos Tolos": (950, 200),
    "Abismo": (800, 750)
}
