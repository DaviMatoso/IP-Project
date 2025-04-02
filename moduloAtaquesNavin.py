import pygame
import random

    class Ability(pygame.sprite.Sprite):
        def __init__(self, pos):
            super().__init__()
            self.image = pygame.image.load('spritesGT/Naturais/um.webp').convert_alpha()
            self.rect = self.image.get_frect(midbottom = pos)
