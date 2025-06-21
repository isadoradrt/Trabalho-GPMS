import pygame
import sys
import os

# Inicialização
pygame.init()
LARGURA, ALTURA = 1280, 720
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Pandemic: Hollow Knight")
FPS = 60
clock = pygame.time.Clock()

# Carregar imagem de fundo
caminho_fundo = os.path.join("designs", "mainscreen.png")
fundo = pygame.image.load(caminho_fundo).convert()
fundo = pygame.transform.scale(fundo, (LARGURA, ALTURA))

# Retângulos clicáveis (valores ajustados manualmente)
botao_novo_jogo = pygame.Rect(30, 337, 400, 50)
botao_continuar = pygame.Rect(30, 408, 400, 50)
botao_opcoes = pygame.Rect(30, 480, 400, 50)
botao_sair = pygame.Rect(30, 553, 400, 50)

def desenhar_menu():
    tela.blit(fundo, (0, 0))
    # (Opcional) para depuração: mostrar as áreas clicáveis
    pygame.draw.rect(tela, (255, 0, 0), botao_novo_jogo, 2)
    pygame.draw.rect(tela, (0, 255, 0), botao_continuar, 2)
    pygame.draw.rect(tela, (0, 0, 255), botao_opcoes, 2)
    pygame.draw.rect(tela, (255, 255, 0), botao_sair, 2)

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
                    print("Novo Jogo iniciado!")
                    rodando = False
                    # Chame sua função de setup do jogo aqui
                elif botao_continuar.collidepoint(evento.pos):
                    print("Continuar jogo (carregar estado salvo)")
                elif botao_opcoes.collidepoint(evento.pos):
                    print("Abrir opções (áudio, controles, etc.)")
                elif botao_sair.collidepoint(evento.pos):
                    print("Saindo do jogo...")
                    pygame.quit()
                    sys.exit()

menu_principal()