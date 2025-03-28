import random
from moduloNAVINimg import NAVIN
from moduloBarraDeVida import barraDeVida
from moduloProjetil import Projetil
from moduloConfig import naturaisLista
from moduloConfig import WIDTH
from moduloConfig import HEIGHT

class Navim():
    def __init__(self, dano, listaFrames):
        self.dead = False
        self.dano = dano
        self.listaFrames = listaFrames
        self.frameAtual = 1
        self.vida = []
        self.Navins = []
        self.proj = []


    def animacaoNavim(self):
        if self.dano > 0:
            self.Navins.append(NAVIN((self.frameAtual)%3, self.listaFrames))
            self.frameAtual += 3

            if self.frameAtual==30:
                self.frameAtual=1
            elif self.frameAtual==31:
                self.frameAtual=2
            elif self.frameAtual==32:
                self.frameAtual=0


    def danoNavim(self, danoEmNavim):
        if self.dano > 0:
            self.dano -= danoEmNavim


    def diminuirVida(self):
        if self.dano > 0:
            self.vida.append(barraDeVida(3000-self.dano))

    def projeteisNavim(self):
        if random.randint(1, 3) == 1:
                self.proj.append(Projetil(naturaisLista, WIDTH))


    def projeteisMove(self):
        if self.dano > 0:
            for projet in self.proj[:]:
                    projet.move()
                    if projet.rect.top > HEIGHT:
                        self.proj.remove(projet)
        elif self.dano<=0:   #apaga com os projeteis qnd navin morre
            self.proj=[]