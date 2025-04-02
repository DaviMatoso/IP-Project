import pygame

#barra de vida class
class barraDeVida:
    def __init__(self, danado):
        self.rect = pygame.Rect(318, 736, 800-(danado*0.266666666), 25) #esse 0.26 so ta ai se a vida do navin for 3000 (800/vida)

        