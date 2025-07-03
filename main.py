import pygame
import sys
import os

from jogo.cidade import criar_cidades
from jogo.jogador import Jogador
from jogo.gerenciador_jogo import GerenciadorJogo
from jogo.constantes import CORES_DOENCAS, CORES_PEOES

pygame.init()
LARGURA, ALTURA = 1280, 720  
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Pandemic: Hollow Knight")
FPS = 60
clock = pygame.time.Clock()
fonte = pygame.font.SysFont("arial", 20)

caminho_base = os.path.dirname(__file__)
caminho_fundo = os.path.join(caminho_base, "designs", "mainscreen.png")
fundo = pygame.image.load(caminho_fundo).convert()
fundo = pygame.transform.scale(fundo, (LARGURA, ALTURA))

#(x, y, largura, altura)
botao_novo_jogo = pygame.Rect(70, 330, 300, 70)
botao_sair = pygame.Rect(130, 550, 150, 60)


botoes_acoes = {
    "Mover": pygame.Rect(50, ALTURA - 60, 120, 40),
    "Tratar": pygame.Rect(190, ALTURA - 60, 120, 40),
}
botao_passar_turno = pygame.Rect(LARGURA - 200, ALTURA - 60, 150, 40)

estado_jogo = {
    "jogo": None,
    "jogador_ativo": None,
}

modo_mover = {"ativo": False}


def desenhar_menu():
    tela.blit(fundo, (0, 0))


def desenhar_jogo(jogo):
    tela.fill((10, 10, 10))

    for cidade in jogo.cidades.values():
        for vizinha in cidade.conexoes:
            if cidade.nome < vizinha.nome:
                pygame.draw.line(tela, (100, 100, 100), cidade.posicao, vizinha.posicao, 2)

    for cidade in jogo.cidades.values():
        x, y = cidade.posicao
        cor_cidade = CORES_DOENCAS.get(cidade.cor, (200, 200, 200))
        pygame.draw.circle(tela, cor_cidade, (x, y), 10)

        nome_render = fonte.render(cidade.nome, True, (255, 255, 255))
        tela.blit(nome_render, (x + 10, y - 10))

        offset_x = 0
        for cor, qtd in cidade.cubos_doenca.items():
            for i in range(qtd):
                pygame.draw.rect(tela, CORES_DOENCAS[cor], (x - 10 + offset_x, y + 12, 6, 6))
                offset_x += 7

    for i, jogador in enumerate(jogo.jogadores):
        x, y = jogador.cidade_atual.posicao
        cor_peao = CORES_PEOES.get(jogador.nome, (255, 255, 0))
        pygame.draw.circle(tela, cor_peao, (x + i * 8, y - 15), 5)

        pygame.draw.circle(tela, cor_peao, (10, 20 + i * 25), 6)

        cartas = ", ".join([c.nome for c in jogador.cartas])
        texto = f"{jogador.nome}: {cartas}"
        texto_render = fonte.render(texto, True, (255, 255, 255))
        tela.blit(texto_render, (25, 10 + i * 25))

    jogador_atual = jogo.jogador_atual
    texto_turno = fonte.render(
        f"Turno de {jogador_atual.nome} - Ações restantes: {jogador_atual.acoes_restantes}",
        True,
        (255, 255, 255)
    )
    tela.blit(texto_turno, (LARGURA - 500, 10))

    if jogador_atual.acoes_restantes > 0:
        for nome, ret in botoes_acoes.items():
            pygame.draw.rect(tela, (50, 50, 200), ret)
            texto = fonte.render(nome, True, (255, 255, 255))
            tela.blit(texto, (ret.x + 10, ret.y + 10))
    else:
        pygame.draw.rect(tela, (200, 50, 50), botao_passar_turno)
        texto = fonte.render("Passar Turno", True, (255, 255, 255))
        tela.blit(texto, (botao_passar_turno.x + 10, botao_passar_turno.y + 10))


def iniciar_jogo():
    cidades = criar_cidades()
    inicio = list(cidades.values())[0]

    jogadores = [
        Jogador("Jogador 1", "Hornet", inicio),
        Jogador("Jogador 2", "Grimm", inicio),
        Jogador("Jogador 3", "Monomon", inicio)
    ]

    jogo = GerenciadorJogo()
    jogo.inicializar_cidades(cidades)
    for j in jogadores:
        jogo.adicionar_jogador(j)

    estado_jogo["jogo"] = jogo
    estado_jogo["jogador_ativo"] = jogo.jogador_atual

    loop_jogo()


def loop_jogo():
    jogo = estado_jogo["jogo"]
    rodando = True
    while rodando:
        clock.tick(FPS)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                pos = evento.pos
                jogador = jogo.jogador_atual

                if modo_mover["ativo"]:
                    for cidade in jogador.cidade_atual.conexoes:
                        x, y = cidade.posicao
                        distancia = ((pos[0] - x) ** 2 + (pos[1] - y) ** 2) ** 0.5
                        if distancia <= 10:
                            jogador.cidade_atual = cidade
                            jogador.acoes_restantes -= 1
                            modo_mover["ativo"] = False
                            print(f"{jogador.nome} se moveu para {cidade.nome}")
                            break

                elif jogador.acoes_restantes > 0:
                    for nome, ret in botoes_acoes.items():
                        if ret.collidepoint(pos):
                            if nome == "Mover":
                                print("Clique em uma cidade conectada para se mover.")
                                modo_mover["ativo"] = True
                            elif nome == "Tratar":
                                for cor in jogador.cidade_atual.cubos_doenca:
                                    if jogador.cidade_atual.cubos_doenca[cor] > 0:
                                        jogador.cidade_atual.cubos_doenca[cor] -= 1
                                        jogador.acoes_restantes -= 1
                                        print(f"{jogador.nome} tratou 1 cubo de {cor} em {jogador.cidade_atual.nome}")
                                        break

                elif botao_passar_turno.collidepoint(pos):
                    print("Passando turno...")
                    jogo.executar_turno()
                    estado_jogo["jogador_ativo"] = jogo.jogador_atual
                    modo_mover["ativo"] = False

        desenhar_jogo(jogo)
        pygame.display.flip()


def menu_principal():
    rodando = True
    while rodando:
        clock.tick(FPS)
        desenhar_menu()
        pygame.display.flip()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if botao_novo_jogo.collidepoint(evento.pos):
                    iniciar_jogo()
                elif botao_sair.collidepoint(evento.pos):
                    pygame.quit()
                    sys.exit()


if __name__ == "__main__":
    menu_principal()
