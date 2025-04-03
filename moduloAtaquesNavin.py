import pygame
import random
from moduloConfig import *

class Ability(pygame.sprite.Sprite):
    def __init__(self, pos, sprite_groups):
        super().__init__(sprite_groups)
        self.image = pygame.image.load(naturaisLista[random.randint(0, 9)]).convert_alpha()
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_frect(midbottom = pos)
        print("Ability position:", self.rect)
        print("Total sprites:", len(sprite_groups))

    def shoot(pos, sprite_groups, num_projectiles = 7, spacing_vertical = 40, spacing_horizontal = 20):
        # Vertical line (|)
        for i in range(num_projectiles):
            y = pos[1] + i * spacing_vertical
            Ability((pos[0], y), sprite_groups)

        # Left diagonal (/)
        for i in range(1, num_projectiles):
            x = pos[0] - i * spacing_horizontal
            y = pos[1] + i * spacing_vertical
            Ability((x, y), sprite_groups)

        # Right diagonal (\)
        for i in range(1, num_projectiles):
            x = pos[0] + i * spacing_horizontal
            y = pos[1] + i * spacing_vertical
            Ability((x, y), sprite_groups)

    def update(self):
        self.rect.centery += 30
        if self.rect.top > HEIGHT:
            self.kill()