#Imports
import pygame
from moduloNAVIN import Navin
from moduloAtaquesNavin import Ability

pygame.init()

#Tela 
WIDTH, HEIGHT = 1440, 810
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Top-Down Shooter")
clock = pygame.time.Clock()
running = True

navin = Navin((720, 150))
golpe = Ability(rect.midtop)

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
    screen.blit(navin.image, navin.rect)

    navin.movement(WIDTH)
    navin.animation()
    navin.attack(screen)

    if navin.ability:
        screen.blit(navin.ability.image, navin.ability.rect)

    pygame.display.flip()
    clock.tick(30)

pygame.quit()