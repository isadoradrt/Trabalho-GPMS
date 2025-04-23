import pygame
import sys
from jogo.constantes import LARGURA, ALTURA, FPS

# Inicialização do Pygame
pygame.init()
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Pandemic")
clock = pygame.time.Clock()


# Loop principal
enquanto_rodando = True

while enquanto_rodando:
   
    clock.tick(FPS)

    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:
            enquanto_rodando = False
                

pygame.quit()
sys.exit()