import pygame
import sys

from cenario import criar_cenario, desenhar_cenario
from cachorro import desenhar_cachorro, mover
from temporizador import desenhar, atualizar
from alimento import gerar_alimento, desenhar_alimento, colidiu_com_jogador
import pontuacao  # 👈 novo

pygame.init()

# 🔤 inicializa fonte da pontuação
pontuacao.iniciar()

largura, altura = 1080, 720
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Pac Dog")

relogio = pygame.time.Clock()

PRETO = (0, 0, 0)

# 🔥 cria o cenário UMA vez só
criar_cenario(largura, altura)

# 🍖 gera o alimento inicial
gerar_alimento(largura, altura)

# ⏱️ estado do temporizador
tempo_inicial = 10
tempo_restante = tempo_inicial
tempo_anterior = pygame.time.get_ticks()
acabou = False

rodando = True
while rodando:
    relogio.tick(60)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    teclas = pygame.key.get_pressed()
    mover(teclas, largura, altura)

    # 🍖 COLISÃO COM ALIMENTO
    if colidiu_com_jogador():
        pontuacao.adicionar_ponto()  # 👈 soma pontos
        gerar_alimento(largura, altura)

    # ⏱️ ATUALIZA O TEMPO
    tempo_anterior, tempo_restante, acabou = atualizar(
        tempo_anterior, tempo_restante, acabou
    )

    if acabou:
        rodando = False

    # 🎨 DESENHO
    tela.fill(PRETO)

    desenhar_cenario(tela)
    desenhar_alimento(tela)
    desenhar_cachorro(tela)

    # 🏆 DESENHA PONTUAÇÃO
    pontuacao.desenhar(tela)

    # ⏱️ DESENHA TEMPORIZADOR
    desenhar(tela, tempo_restante)

    pygame.display.flip()

pygame.quit()
sys.exit()