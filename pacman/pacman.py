import pygame

PRETO = (0, 0, 0)
AMARELO = (255, 255, 0)
VELOCIDADE = 1
RAIO = 50

pygame.init()

tela = pygame.display.set_mode((640, 480), 0)
x = 10
velocidade_x = 1
y = 25
velocidade_y = 1
while True:
    # Calcula regras
    x = x + velocidade_x
    y = y + velocidade_y
    if x + RAIO > 640:
        velocidade_x = -VELOCIDADE
    if x - RAIO  < 0:
        velocidade_x = VELOCIDADE
    if y + RAIO > 480:
        velocidade_y = -VELOCIDADE
    if y - RAIO < 0:
        velocidade_y = VELOCIDADE

    # Pinta
    tela.fill(PRETO)
    pygame.draw.circle(tela, AMARELO, (int(x), int(y)), RAIO, 0)
    pygame.display.update()

    #Eventos
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()
