#Imports
import time
import pygame
import random
from moduloConfig import *
from moduloPlayer import Player
from moduloBarraDeVida import barraDeVida
from moduloDesenhoVida import healthBar
from moduloNAVIN import NAVIN
from moduloEnemy import Enemy
from moduloProjetil import Projetil
from moduloArmaAtiva import armaAtiva
from moduloDesenho import *
from moduloColisão import ColisaoMapa
from moduloVidaPlayer import vidaPlayer
from moduloVazio import Vazio
from moduloColetaveis import *

def game_over_screen(rodando):
    keys = pygame.key.get_pressed()
    screen.fill(BLACK)
        
    # Renderizar textos
    text = font.render("GAME OVER", True, RED)
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 3))
    
    retry_text = small_font.render("Pressione ESPAÇO para jogar novamente", True, WHITE)
    retry_rect = retry_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))

    quit_text = small_font.render("Pressione ESC para sair", True, WHITE)
    quit_rect = quit_text.get_rect(center=(WIDTH // 2, HEIGHT // 1.5))

    # Desenhar na tela
    screen.blit(text, text_rect)
    screen.blit(retry_text, retry_rect)
    screen.blit(quit_text, quit_rect)
    
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    return
                if event.key == pygame.K_SPACE:
                    fase2()
                    return

def fase2():
    # Carregar a imagem de fundo
    background = pygame.image.load("spritesGT/Map_2.png")
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))  # Ajustar o tamanho da imagem do fundo

    clock = pygame.time.Clock()
    player = Player(player_size2, player_size, WIDTH, HEIGHT)
    dano = 3000      #vida do navin
    health_bar = healthBar() # Load da barra de vida
    
    #Lista de objetos moviveis gerados
    bullets = []
    enemies = []
    proj = []
    vazio=[]
    score = 0
    numeroNavin=0
    running = True
    lastDmg = 0
    x=['spritesGT/bombaVazio.png']

    vidaJogador = vidaPlayer()
    vidaJogador.adicionarCoracao(3)

    pistola = armaAtiva(0.5, 20, 21, 100, 1)
    metralhadora = armaAtiva(0.0, 30, 10, 10, 1)
    bazuca = armaAtiva(2, 10, 70, 500, 1)
    escopeta = armaAtiva(0.5,20, 15, 70, 5)

    armaAtual = pistola
    arma = 'pistola'
    inventorioArmas = [pistola, metralhadora]

    listaBlocos = [(pygame.Rect(0, 0, 241, 810)), 
    (pygame.Rect(150, 0, 1140, 292)),
    (pygame.Rect(1210, 0, 300, 810)),
    (pygame.Rect(150, 720, 490, 292)),
    (pygame.Rect(820, 720, 495, 90)),
    (pygame.Rect(150, 1101, 165, 90)),
    (pygame.Rect(518, 292, 413, 257)),
    (pygame.Rect(-1, -1, 1440, 1)),
    (pygame.Rect(0, 811, 1440, 1))]


    while running:      #LOOP DE RODAR
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    
        screen.blit(background, (0, 0))  #
        screen.blit(player.image, player.rect)  

        #movimento do player
        keys = pygame.key.get_pressed()        #Teclas de movi do player
        dx = keys[pygame.K_d] - keys[pygame.K_a]
        dy = keys[pygame.K_s] - keys[pygame.K_w]
        player.move(dx, dy, player_speed, listaBlocos)

        #Spawn de bullet
        keys = pygame.key.get_pressed()
        var = armaAtual.shoot(keys, player.rect.centerx, player.rect.top, bullets, arma)
        if var is not None:
            bullets.append(var)

        #Movimento de bullet 
        armaAtual.bullet_movement(bullets)

        #Spawn nivan (NÃO TOQUE NESSA LIST)
        navins = []
        vida =[]
        if dano > 0:
            health_bar.printar(screen) # Blit da barra de vida 
            vida.append(barraDeVida(3000-dano))
            #Spawn projetil
            if random.randint(1, 30) == 1 and len(vazio)<1:
                tickSpawnVazio=pygame.time.get_ticks()
                a=random.randint(1200, 2000)
                vazio.append(Vazio(x, WIDTH))
            if len(vazio)==1:
                navinListaAtk=['spritesGT/navin_attack.png']
                numeroNavinAtk=0
                navins.append(NAVIN(numeroNavinAtk, navinListaAtk))
            else:            
                navins.append(NAVIN(numeroNavin%3, navinLista))
            #Movimento de projetil
            for projV in vazio:
                projV.printar(vazio)
                expX=vazio[-1].rect.x-90
                expY=vazio[-1].rect.y-90
                projV.moveVazio(tickSpawnVazio, a)
                if pygame.time.get_ticks() >= tickSpawnVazio+(a):
                    explosao=pygame.Rect(expX, expY, 200, 200)
                    screen.blit(pygame.transform.scale((pygame.image.load('spritesGT/Explosao.png')), (200, 200)), explosao)
                    if pygame.time.get_ticks()>tickSpawnVazio+(a)+300:
                        if explosao.colliderect(player):
                            if len(vidaJogador.vida) > 1:
                                vidaJogador.retirarCoracao(1)
                            else:    
                                game_over_screen(running)
                        vazio.remove(projV)
            if random.randint(1, 5) == 1:
                proj.append(Projetil(naturaisLista, WIDTH))
            #Movimento de projetil
            for projet in proj[:]:
                projet.move()
                if projet.rect.y > HEIGHT:
                    proj.remove(projet)

        elif dano<=0:   #apaga com os projeteis qnd navin morre
            proj=[]
            vazio=[]
            listaBlocos = [(pygame.Rect(0, 0, 241, 810)), 
                        (pygame.Rect(150, 0, 500, 292)),
                        (pygame.Rect(795, 0, 495, 292)),
                        (pygame.Rect(1210, 0, 300, 810)),
                        (pygame.Rect(150, 720, 490, 292)),
                        (pygame.Rect(820, 720, 495, 90)),
                        (pygame.Rect(150, 1101, 165, 90)),
                        (pygame.Rect(518, 292, 132, 257)),
                        (pygame.Rect(795, 292, 136, 257)),
                        (pygame.Rect(-1, 60, 1440, 1)),
                        (pygame.Rect(0, 811, 1440, 1)),
                        ]
            #if player.rect.x>710 and player.rect.y<40:
            #    fase2()
    
        #Tick de animacao do navin
        if numeroNavin==30:  
            numeroNavin=1
        elif numeroNavin==31:
            numeroNavin=2
        elif numeroNavin==32:
            numeroNavin=0

        #Colisão bullet com navin
        for bullet in bullets:
            for navin in navins:
                if bullet.rect.colliderect(navin.rect):
                    dano -= bullet.danoBala
                    bullets.remove(bullet)

        #Desenho player, fundo, bullet
        printar=desenhar(screen, BLACK, RED, WHITE, bullets, enemies, navins, proj, vida, listaBlocos, player, vidaJogador.vida, vazio)
        printar
        
        #troca de armas
        arma, armaAtual=armaAtiva.escolha(keys, pistola, metralhadora, bazuca, escopeta, armaAtual, arma, inventorioArmas)
        

        #Score (ADD VIDA, ARMA, VIDA NAVIN)
        font = pygame.font.Font(None, 36)
        score_text = font.render(f'Score: {score}', True, BLACK)
        screen.blit(score_text, (10, 10))

        #Tela de gameover (cogitar sistema de vida no lugar do hit kill)

        currentTime = time.time()

        for projes in proj:
            if player.rect.colliderect(projes.rect):
                if currentTime - lastDmg > 0.5:
                    if len(vidaJogador.vida) > 1:
                        vidaJogador.retirarCoracao(1)
                    else:    
                        game_over_screen(running)
                    lastDmg = currentTime

        #Comando pygame (NAO TOQUE)
        pygame.display.flip()
        numeroNavin+=3 #é 3 pq tem 4 imagens de navin
        clock.tick(30)

    #NAO TOQUE
    pygame.quit()
