from funcoes import desenhar_poligono, scanline_fill
from cenario import MESAS, LARGURA_MESA, ALTURA_MESA
import pygame
# Cores
MARROM = (139, 69, 19)
BRANCO = (255, 255, 255)

# Tamanho
TAMANHO = 40

# Posição inicial (centro)
x = 540
y = 360

# Velocidade
VELOCIDADE = 5

def mover(teclas, largura_tela, altura_tela):
    global x, y

    novo_x = x
    novo_y = y

    if teclas[pygame.K_w] or teclas[pygame.K_UP]:
        novo_y -= VELOCIDADE
    if teclas[pygame.K_s] or teclas[pygame.K_DOWN]:
        novo_y += VELOCIDADE
    if teclas[pygame.K_a] or teclas[pygame.K_LEFT]:
        novo_x -= VELOCIDADE
    if teclas[pygame.K_d] or teclas[pygame.K_RIGHT]:
        novo_x += VELOCIDADE

    metade = TAMANHO // 2

    # Limite da tela
    if novo_x - metade < 0:
        novo_x = metade
    if novo_x + metade > largura_tela:
        novo_x = largura_tela - metade
    if novo_y - metade < 0:
        novo_y = metade
    if novo_y + metade > altura_tela:
        novo_y = altura_tela - metade

    # 🔥 COLISÃO COM MESA
    if not colidiu_com_mesa(novo_x, novo_y):
        x = novo_x
        y = novo_y

def colidiu_com_mesa(novo_x, novo_y):
    metade = TAMANHO // 2

    # limites do cachorro
    cachorro_esq = novo_x - metade
    cachorro_dir = novo_x + metade
    cachorro_top = novo_y - metade
    cachorro_bot = novo_y + metade

    for (mx, my) in MESAS:
        mesa_esq = mx
        mesa_dir = mx + LARGURA_MESA
        mesa_top = my
        mesa_bot = my + ALTURA_MESA

        # teste de interseção de retângulos (AABB)
        if (
            cachorro_dir > mesa_esq and
            cachorro_esq < mesa_dir and
            cachorro_bot > mesa_top and
            cachorro_top < mesa_bot
        ):
            return True

    return False


def desenhar_cachorro(superficie):
    metade = TAMANHO // 2

    pontos = [
        (x - metade, y - metade),
        (x + metade, y - metade),
        (x + metade, y + metade),
        (x - metade, y + metade)
    ]

    scanline_fill(superficie, pontos, MARROM)
    desenhar_poligono(superficie, pontos, BRANCO)