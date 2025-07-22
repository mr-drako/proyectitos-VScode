import pygame
from pygame.locals import *
pygame.init()
color=pygame.Color(0,0,0)
ventana=pygame.display.set_mode((1600,900))
imagen=pygame.image.load("archivos/perro dinosaurio.png")
pygame.display.set_caption("dinodog bouncing")
XP,YP=115,65
ventana.fill(color)
vx=2
vy=2
while True:
    ventana.blit(imagen,(XP,YP))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
        elif event.type==KEYDOWN:
            pygame.quit()
    XP+=vx
    YP+=vy
    ventana.fill(color)
    if XP<115 or XP>1285:
        vx=-vx
    if YP<65 or YP>650:
        vy=-vy

        