#Imports
import pygame
from moduloNAVIN import Navin
from moduloAtaquesNavin import Ability
from moduloConfig import *

pygame.init()

#Tela 
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Top-Down Shooter")
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
running = True

navin = Navin((720, 150), all_sprites)

# Main game loop
while running:


    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Carregar a imagem de fundo
    background = pygame.image.load("spritesGT/Map_1.png")
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))  # Ajustar o tamanho da imagem do fundo

    screen.blit(background, (0, 0))

    navin.movement(WIDTH)
    navin.animation()
    navin.attack()

    all_sprites.update()
    all_sprites.draw(screen)

    pygame.display.flip()
    clock.tick(30)

pygame.quit()