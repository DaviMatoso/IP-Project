#Imports
import pygame
from moduloNAVIN import Navin

#Comando pygame (NAO TOQUE)
pygame.init()

#Tela 
WIDTH, HEIGHT = 1440, 810
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Top-Down Shooter")
clock = pygame.time.Clock()
running = True

navin = Navin((720, 150))

# Main game loop
while running:


    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Carregar a imagem de fundo
    background = pygame.image.load("spritesGT/Map_1.png")
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))  # Ajustar o tamanho da imagem do fundo

    navin.movement(WIDTH)
    navin.animation()

    screen.blit(background, (0, 0))
    screen.blit(navin.image, navin.rect)

    #Comando pygame (NAO TOQUE)
    pygame.display.flip()
    clock.tick(30)

pygame.quit()