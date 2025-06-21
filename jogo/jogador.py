from cartas import CartaCidade

class Jogador:
    def __init__(self, nome, personagem, cidade_inicial, cartas=None):
        self.nome = nome
        self.personagem = personagem  # Ex: "Knight", "Hornet"
        self.cidade_atual = cidade_inicial  # Objeto CartaCidade
        self.cartas = cartas or []  # Lista de cartas do jogador
        self.acoes_restantes = 4

    def mover_para(self, nova_cidade):
        if nova_cidade in self.cidade_atual.conexoes:
            self.cidade_atual = nova_cidade
            self.acoes_restantes -= 1
            print(f"{self.nome} moveu-se para {nova_cidade.nome}")
        else:
            print("Cidade não conectada.")

    def tratar_doenca(self):
        if self.cidade_atual.tem_doenca():
            self.cidade_atual.remover_doenca()
            self.acoes_restantes -= 1
            print(f"{self.nome} tratou uma doença em {self.cidade_atual.nome}")
        else:
            print("Não há doença para tratar.")

    def descobrir_cura(self, cor_doenca):
        cartas_da_cor = [c for c in self.cartas if c.cor == cor_doenca]
        if len(cartas_da_cor) >= 5:
            for c in cartas_da_cor[:5]:
                self.cartas.remove(c)
            self.acoes_restantes -= 1
            print(f"{self.nome} descobriu a cura para {cor_doenca}")
        else:
            print("Cartas insuficientes para descobrir cura.")

    def adicionar_carta_mao(self, carta):
        if len(self.cartas) < 7:
            self.cartas.append(carta)
            print(f"{self.nome} pegou a carta {carta.nome}")
        else:
            print(f"{self.nome} já está com 7 cartas na mão!")

    def remover_carta_mao(self, carta):
        if carta in self.cartas:
            self.cartas.remove(carta)
            print(f"{self.nome} descartou a carta {carta.nome}")

    def compartilhar_carta(self, outro_jogador, carta):
        if carta in self.cartas and self.cidade_atual == outro_jogador.cidade_atual:
            self.cartas.remove(carta)
            outro_jogador.cartas.append(carta)
            self.acoes_restantes -= 1
            print(f"{self.nome} compartilhou a carta {carta.nome}")
        else:
            print("Condições para compartilhar carta não atendidas.")

    def __str__(self):
        return f"{self.nome} ({self.personagem}) - {self.cidade_atual.nome}"