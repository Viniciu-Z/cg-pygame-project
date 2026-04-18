from funcoes import desenhar_poligono, scanline_fill
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

def mover(teclas):
    global x, y

    if teclas[pygame.K_w] or teclas[pygame.K_UP]:
        y -= VELOCIDADE
    if teclas[pygame.K_s] or teclas[pygame.K_DOWN]:
        y += VELOCIDADE
    if teclas[pygame.K_a] or teclas[pygame.K_LEFT]:
        x -= VELOCIDADE
    if teclas[pygame.K_d] or teclas[pygame.K_RIGHT]:
        x += VELOCIDADE


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