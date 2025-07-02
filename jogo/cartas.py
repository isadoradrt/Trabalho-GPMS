from enum import Enum

class TipoCarta(Enum):
    CIDADE = "Cidade"
    EVENTO = "Evento"
    EPIDEMIA = "Epidemia"

class Carta:
    def __init__(self, nome: str, tipo: TipoCarta, cor: str = None, descricao: str = None):
        self.nome = nome
        self.tipo = tipo
        self.cor = cor
        self.descricao = descricao

    def __str__(self):
        if self.tipo == TipoCarta.CIDADE:
            return f"{self.tipo.value}: {self.nome} ({self.cor})"
        elif self.tipo == TipoCarta.EVENTO:
            return f"{self.tipo.value}: {self.nome} - {self.descricao}"
        else:
            return f"{self.tipo.value}: {self.nome}"
