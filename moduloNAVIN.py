import pygame
from moduloConfig import *

#navin class
class NAVIN:
    def __init__(self, numeroNavin, navinLista):
        self.image = pygame.image.load(navinLista[numeroNavin])  # Carregar imagem do jogador
        self.image = pygame.transform.scale(self.image, (267, 315))  # Ajustar o tamanho da imagem
        self.rect = self.image.get_rect(center=(720, 150))  # Usar o retângulo da imagem

        self.direcaoNavin = pygame.math.Vector2(1, 0)
        self.velocidadeNavin = 10

    def movimento(self):

        if self.rect.right > WIDTH or self.rect.left < 0:
            self.direcaoNavin.x *= -1
        self.rect.center += self.direcaoNavin * self.velocidadeNavin