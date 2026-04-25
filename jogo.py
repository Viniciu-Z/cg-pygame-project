import pygame
import sys
import viewport

from cenario import criar_cenario, desenhar_cenario
from cachorro import desenhar_cachorro, mover
from temporizador import desenhar as desenhar_tempo, atualizar
from alimento import gerar_alimento, desenhar_alimento, colidiu_com_jogador
import pontuacao

PRETO = (0, 0, 0)

pygame.init()

largura, altura = 1080, 720
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Pac Dog")

relogio = pygame.time.Clock()

# Inicializa sistemas
pontuacao.iniciar()

# Cria cenário
criar_cenario(largura, altura)

# Gera primeiro alimento
gerar_alimento(largura, altura)

# Controle de tempo
tempo_inicial = 50
tempo_restante = tempo_inicial
tempo_anterior = pygame.time.get_ticks()
acabou = False

rodando = True
while rodando:
    relogio.tick(60)

    # Eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    # Entrada e movimento
    teclas = pygame.key.get_pressed()
    mover(teclas, largura, altura)

    # Colisão com alimento
    if colidiu_com_jogador():
        pontuacao.adicionar_ponto()
        gerar_alimento(largura, altura)

    # Atualização do tempo
    tempo_anterior, tempo_restante, acabou = atualizar(
        tempo_anterior, tempo_restante, acabou
    )

    if acabou:
        rodando = False

    # Renderização
    tela.fill(PRETO)

    desenhar_cenario(tela)
    desenhar_alimento(tela)
    desenhar_cachorro(tela)

    pontuacao.desenhar(tela)
    desenhar_tempo(tela, tempo_restante)
    viewport.desenhar_minimapa(tela, largura, altura)

    pygame.display.flip()

pygame.quit()
sys.exit()