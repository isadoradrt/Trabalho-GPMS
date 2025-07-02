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

CONEXOES = {
    "Penhascos Uivantes": ["Dirtmouth", "Caminho Verde"],
    "Dirtmouth": ["Penhascos Uivantes", "Pico de Cristal", "Encruzilhada Esquecida"],
    "Pico de Cristal": ["Dirtmouth", "Encruzilhada Esquecida", "Terra do Descanso"],
    "Caminho Verde": ["Jardins da Rainha", "Encruzilhada Esquecida", "Penhascos Uivantes", "Cânion da Névoa"],
    "Encruzilhada Esquecida": ["Dirtmouth", "Terra do Descanso", "Caminho Verde", "Pico de Cristal", "Ermos Fúngicos"],
    "Jardins da Rainha": ["Caminho Verde", "Ermos Fúngicos", "Cânion da Névoa", "Ninho Profundo"],
    "Cânion da Névoa": ["Caminho Verde", "Ermos Fúngicos", "Jardins da Rainha"],
    "Ermos Fúngicos": ["Cânion da Névoa", "Jardins da Rainha", "Cidade das Lágrimas", "Encruzilhada Esquecida", "Vila dos Louva-a-Deus"],
    "Cidade das Lágrimas": ["Ermos Fúngicos", "Terra do Descanso", "Borda do Reino", "Hidrovia Real"],
    "Ninho Profundo": ["Vila dos Louva-a-Deus", "Jardins da Rainha", "Bacia Antiga"],
    "Hidrovia Real": ["Cidade das Lágrimas", "Vila dos Louva-a-Deus", "Bacia Antiga"],
    "Bacia Antiga": ["A Colmeia", "Ninho Profundo", "Abismo", "Hidrovia Real"],
    "Borda do Reino": ["Cidade das Lágrimas", "A Colmeia", "Coliseu dos Tolos"],
    "A Colmeia": ["Bacia Antiga", "Borda do Reino"],
    "Terra do Descanso": ["Pico de Cristal", "Cidade das Lágrimas", "Encruzilhada Esquecida"],
    "Vila dos Louva-a-Deus": ["Ninho Profundo", "Ermos Fúngicos", "Hidrovia Real"],
    "Coliseu dos Tolos": ["Borda do Reino"],
    "Abismo": ["Bacia Antiga"]
}


def criar_cidades():
    cidades = {
        nome: Cidade(nome, cor, POSICOES_CIDADES[nome])
        for nome, cor in CIDADES.items()
        if nome in POSICOES_CIDADES
    }

    # Conectando as cidades de forma clara e limpa
    for nome, vizinhas in CONEXOES.items():
        for vizinha in vizinhas:
            if nome in cidades and vizinha in cidades:
                cidades[nome].conectar(cidades[vizinha])

    return cidades
