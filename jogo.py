import pygame
import sys

from cenario import criar_cenario, desenhar_cenario
from cachorro import desenhar_cachorro, mover

pygame.init()

largura, altura = 1080, 720
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Pac Dog")

relogio = pygame.time.Clock()

PRETO = (0, 0, 0)

# 🔥 cria o cenário UMA vez só (otimização principal)
criar_cenario(largura, altura)

rodando = True
while rodando:
    relogio.tick(60)   # tempo em segundos

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    teclas = pygame.key.get_pressed()
    mover(teclas, largura, altura)

    # 🎨 desenho
    tela.fill(PRETO)

    desenhar_cenario(tela)
    desenhar_cachorro(tela)

    pygame.display.flip()

pygame.quit()
sys.exit()