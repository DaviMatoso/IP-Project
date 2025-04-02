import pygame
from os.path import join
from os import walk

class Navin(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.carregarImagens()
        self.state, self.frame_index = 'idle', 0
        self.image = pygame.image.load(join('spritesGT', 'navin', 'idle', '0.png')).convert_alpha()
        self.rect = self.image.get_frect(center = pos)

        self.pos = pygame.Vector2(pos)
        self.direcaoNavin = pygame.Vector2(1, 0)
        self.velocidadeNavin = 8

    def carregarImagens(self):
        self.frames = {'idle': [], 'ataque': []}

        for state in self.frames.keys():
            for folder_path, sub_folders, file_names in walk(join('spritesGT', 'navin', state)):
                if file_names:
                    for file_name in sorted(file_names, key = lambda name: int(name.split('.')[0])):
                        full_path = join(folder_path, file_name)
                        surf = pygame.image.load(full_path).convert_alpha()
                        self.frames[state].append(surf)


    def movement(self, screen_width):
        self.rect.x += self.direcaoNavin.x * self.velocidadeNavin
        if self.rect.right > screen_width or self.rect.left < 0:
            self.direcaoNavin *= -1

    def animation(self):

        self.frame_index += 0.2
        self.image = self.frames[self.state][int(self.frame_index) % len(self.frames[self.state])]