# Baralho do Pandemic:

# Baralho de jogador
#           Cartas de cidade: Usadas para movimento ou curas.
#           Cartas de evento: Habilidades especiais (ex: "Voar charter", "Quarentena").

# Baralho de infecção
#           Cartas de cidade - precisam de cor (elas representam uma doença de uma das 4 cores: azul, amarelo, preto ou vermelho).
#           Cartas de Epidemia
#                     Aumentam a taxa de infecção.
#                     Infectam uma cidade aleatória com 3 cubos.
#                     Reembaralham as cartas descartadas de infecção.


from enum import Enum

class TipoCarta(Enum):
    CIDADE = "Cidade"
    EVENTO = "Evento"
    EPIDEMIA = "Epidemia"

class Carta:
    def __init__(self, nome: str, tipo: TipoCarta, cor: str = None, descricao: str = None):
        self.nome = nome
        self.tipo = tipo
        self.cor = cor  # Só faz sentido para cartas de cidade
        self.descricao = descricao  # Só faz sentido para eventos ou epidemias

    def __str__(self):
        return f"{self.tipo.value}: {self.nome}" + (f" ({self.cor})" if self.cor else "")

