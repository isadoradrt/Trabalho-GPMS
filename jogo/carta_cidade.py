from cartas import Carta, TipoCarta

class CartaCidade(Carta):
    def __init__(self, nome, cor):
        super().__init__(nome, TipoCarta.CIDADE, cor)

    def __str__(self):
        return f"Cidade - {self.nome} ({self.cor})"