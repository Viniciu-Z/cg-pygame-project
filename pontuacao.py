import pygame

PRETO = (0, 0, 0)

# 🔢 variável global de pontos
pontos = 0

# 🔤 fonte (inicializada uma vez)
fonte = None


def iniciar():
    global fonte
    fonte = pygame.font.SysFont(None, 36)

def adicionar_ponto():
    global pontos
    pontos += 50

def resetar():
    global pontos
    pontos = 0

def desenhar(tela):
    texto = fonte.render(f"Pontos: {pontos}", True, PRETO)
    tela.blit(texto, (10, 10))