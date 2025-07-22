pip install pygame
import pygame
from pygame.locals import *
from random import randint
class Serpiente:
    #serpiente solo sera printiable en un tablero
    #agregar funcion que tire que cree la serpiente usando ASCII o el formato <----┑┕----┙||┌ ("pbody(self)")
    def __init__(self,f,c):
        self.row=int(f)
        self.col=int(c)
        self.head=[f,c]
        self.body=[]
        self.dir="w"
    def move(self,dir):
        self.dir=dir
        for i in range(1,len(self.body)-1):
            self.body[i]=self.body[i-1]
        self.body[0]=self.head
        if self.dir == "w":
            self.head[0]-=1
        elif self.dir=="s":
            self.head[0]+=1
        elif self.dir=="a":
            self.head[1]-=1
        elif self.dir=="d":
            self.head[1]+=1
        return self.head
    def eat(self):
        if len(self.body)==0:
            pass
        else:
            Δc=self.body[-2][1]-self.body[-1][1]
            Δf=self.body[-2][0]-self.body[-1][0]
            if Δc==0:
                if Δf<0:
                    self.body.append([self.body[-1][0]-1,self.body[-1][1]])
                else:
                    self.body.append([self.body[-1][0]+1,self.body[-1][1]])
            else:
                if Δc<0:
                    self.body.append([self.body[-1][0],self.body[-1][1]+1])
                else:
                    self.body.append([self.body[-1][0],self.body[-1][1]-1])
    def viva(self):
        c=True
        for e in self.body:
            if e==self.head:
                c=False
        return c
class Comida:
    def __init__(self):
        pass
    def __str__(self):
        return "@"

#muy sujeta a cambios, definir el tablero como lista de serpiente comida o celdas
#gen deberia agregar a la serpiente y la comida en el tablero
class Tablero:
    def __init__(self,dim):
        self.tablero=[]
        self.dim=int(dim)
    def gen(self):
        for j in range(self.dim):
            (self.tablero.append(["· " for i in range(self.dim)])) 
    def __str__(self):
        #cambiarlo para que imprima la serpiente y la comida
        t=" "
        for i in range(self.dim):
            t=t+"· "*self.dim+"\n "
        return t
pygame.init()
pan=pygame.display.set_mode([1680,720])
pygame.display.set_caption("Snake")
play=True
while play:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            play=False
    pygame.display.flip()
