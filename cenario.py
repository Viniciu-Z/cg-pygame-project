from funcoes import desenhar_poligono

# Cor padrão das mesas
COR_MESA = (255, 255, 255)

# Dimensões
LARGURA_MESA = 400
ALTURA_MESA = 235

# Posições
MESAS = [
    (70, 70),
    (600, 70),
    (70, 410),
    (600, 410)
]

def desenhar_mesa(superficie, x, y):
    pontos = [
        (x, y),
        (x + LARGURA_MESA, y),
        (x + LARGURA_MESA, y + ALTURA_MESA),
        (x, y + ALTURA_MESA)
    ]

    desenhar_poligono(superficie, pontos, COR_MESA)


def desenhar_cenario(superficie):
    for (x, y) in MESAS:
        desenhar_mesa(superficie, x, y)