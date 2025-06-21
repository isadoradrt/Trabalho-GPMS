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

