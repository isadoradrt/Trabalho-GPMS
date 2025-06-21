class Doenca:
    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor
        self.cura_descoberta = False

    def descobrir_cura(self):
        self.cura_descoberta = True
        print(f"Cura da doença {self.nome} foi descoberta!")

    def __str__(self):
        status = "Curada" if self.cura_descoberta else "Não curada"
        return f"{self.nome} ({self.cor}) - {status}"
