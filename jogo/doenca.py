class Doenca:
    def __init__(self, cor):
        self.cor = cor
        self.curada = False
        self.erradicada = False

    def curar(self):
        self.curada = True

    def erradicar(self):
        self.erradicada = True
        self.curada = True  

    def __str__(self):
        status = "erradicada" if self.erradicada else "curada" if self.curada else "ativa"
        return f"Doença {self.cor} - {status}"
