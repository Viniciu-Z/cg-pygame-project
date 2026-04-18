import pygame
import sys
from cenario import desenhar_cenario

pygame.init()

largura, altura = 1080, 720
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Set Pixel")

PRETO = (0, 0, 0)

rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    tela.fill(PRETO)

    desenhar_cenario(tela)

    pygame.display.flip()

pygame.quit()
sys.exit()