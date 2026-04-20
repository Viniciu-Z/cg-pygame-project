import random
from funcoes import gerar_elipse, scanline_fill, desenhar_poligono
from cenario import MESAS, LARGURA_MESA, ALTURA_MESA
import cachorro

# 🎨 Cor
VERMELHO = (255, 0, 0)

# 📏 Tamanho
TAMANHO_ALIMENTO = 20

# 📍 Posição inicial
x = 0
y = 0

def gerar_alimento(largura_tela, altura_tela):
    global x, y

    while True:
        novo_x = random.randint(TAMANHO_ALIMENTO, largura_tela - TAMANHO_ALIMENTO)
        novo_y = random.randint(TAMANHO_ALIMENTO, altura_tela - TAMANHO_ALIMENTO)

        if not dentro_da_mesa(novo_x, novo_y) and not perto_do_cachorro(novo_x, novo_y):
            x = novo_x
            y = novo_y
            break

def dentro_da_mesa(px, py):
    for (mx, my) in MESAS:
        if (
            px > mx and
            px < mx + LARGURA_MESA and
            py > my and
            py < my + ALTURA_MESA
        ):
            return True
    return False

def perto_do_cachorro(px, py):
    metade = TAMANHO // 2

    if (
        px > dog_x - metade and
        px < dog_x + metade and
        py > dog_y - metade and
        py < dog_y + metade
    ):
        return True

    return False

def desenhar_alimento(superficie):
    pontos = gerar_elipse(x, y, TAMANHO_ALIMENTO // 2, TAMANHO_ALIMENTO // 2, passos=50)
    scanline_fill(superficie, pontos, VERMELHO)
    desenhar_poligono(superficie, pontos, (0, 0, 0))

from cachorro import x as dog_x, y as dog_y, TAMANHO

def colidiu_com_jogador():
    metade_dog = cachorro.TAMANHO // 2
    metade_food = TAMANHO_ALIMENTO // 2

    # pega posição ATUAL do cachorro
    dog_x = cachorro.x
    dog_y = cachorro.y

    # bounding box do cachorro
    dog_esq = dog_x - metade_dog
    dog_dir = dog_x + metade_dog
    dog_top = dog_y - metade_dog
    dog_bot = dog_y + metade_dog

    # bounding box do alimento
    food_esq = x - metade_food
    food_dir = x + metade_food
    food_top = y - metade_food
    food_bot = y + metade_food

    # colisão AABB
    if (
        dog_dir > food_esq and
        dog_esq < food_dir and
        dog_bot > food_top and
        dog_top < food_bot
    ):
        return True

    return False