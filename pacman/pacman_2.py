import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600), 0)

AMARELO = (255, 255, 0)
PRETO = (0, 0, 0)
VELOCIDADE = 1
PARADO = 0

class Pacman:
    def __init__(self):
        self.coluna = 1
        self.linha = 1
        self.centro_x = 400
        self.centro_y = 300
        self.tamanho = 800 // 30
        self.velocidade_x = 0
        self.velocidade_y = 0
        self.raio = self.tamanho // 2

    def calcular_regras(self):
        self.coluna = self.coluna + self.velocidade_x
        self.linha = self.linha + self.velocidade_y
        # falta arrumar contato com as bordas da tela
        self.centro_x = int(self.coluna * self.tamanho + self.raio)
        self.centro_y = int(self.linha * (self.tamanho + self.raio))

    def pintar(self, tela):
        # desenha o corpo do pacman
        pygame.draw.circle(tela, AMARELO, (self.centro_x, self.centro_y), self.raio, 0)

        # desenho da boca do pacman
        canto_boca = (self.centro_x, self.centro_y)
        labio_superior = (self.centro_x + self.raio, self.centro_y - self.raio)
        labio_inferior = (self.centro_x + self.raio, self.centro_y)
        pontos = [canto_boca, labio_superior, labio_inferior]
        pygame.draw.polygon(tela, PRETO, pontos, 0)

        # desenho do olho do pacman
        olho_x = int(self.centro_x + self.raio / 3)
        olho_y = int(self.centro_y - self.raio * 0.7)
        olho_raio = int(self.raio / 8)
        pygame.draw.circle(tela, PRETO, (olho_x, olho_y), olho_raio, 0)


    def processar_eventos(self, eventos):
        for e in eventos:
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_RIGHT:
                    self.velocidade_x = VELOCIDADE
                elif e.key == pygame.K_LEFT:
                    self.velocidade_x = -VELOCIDADE
                elif e.key == pygame.K_UP:
                    self.velocidade_y = -VELOCIDADE
                elif e.key == pygame.K_DOWN:
                    self.velocidade_y = VELOCIDADE
            elif e.type == pygame.KEYUP:
                if e.key == pygame.K_RIGHT:
                    self.velocidade_x = PARADO
                elif e.key == pygame.K_LEFT:
                    self.velocidade_x = PARADO
                elif e.key == pygame.K_UP:
                    self.velocidade_y = PARADO
                elif e.key == pygame.K_DOWN:
                    self.velocidade_y = PARADO


if __name__ == "__main__":
    pacman = Pacman()

    while True:
        # calcula as regras
        pacman.calcular_regras()

        # pinta a tela
        screen.fill(PRETO)
        pacman.pintar(screen)
        pygame.display.update()
        pygame.time.delay(100)

        # captura os eventos
        eventos = pygame.event.get()
        for e in eventos:
            if e.type == pygame.QUIT:
                exit()
        pacman.processar_eventos(eventos)
