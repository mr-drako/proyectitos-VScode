from __future__ import annotations
import math
import pygame
from random import randint
from pygame.locals import *

class Particula:

    num = 1

    def __init__(self, ventana: pygame.surface.Surface, color: pygame.color.Color, 
                 posicion: tuple, radio: int, velocidad: tuple):
        self.ventana = ventana
        self.color = color
        self.radio = radio
        self.particula = pygame.draw.circle(ventana, color, posicion, radio)
        self.velocidad = velocidad
        self._posicion = list(posicion)
        self.num = Particula.num
        Particula.num += 1
    @property
    def posicion(self) -> list:
        return tuple(self._posicion)
    
    @posicion.setter
    def posicion(self, nueva_posicion: tuple) -> None:
        limite_y = self.ventana.get_height() - self.radio
        limite_x = self.ventana.get_width() - self.radio
        new_pos_x, new_pos_y = nueva_posicion
        
        #control limites en x
        if new_pos_x >= limite_x: 
            new_pos_x = limite_x - 1
        elif new_pos_x < self.radio:
            new_pos_x = self.radio + 1
        
        #control limites en y
        if new_pos_y >= limite_y:
            new_pos_y = limite_y - 1 
        elif new_pos_y < self.radio:
            new_pos_y = self.radio + 1 
       
        self._posicion = [new_pos_x, new_pos_y]

    def avanzar(self) -> None:
        limite_y = self.ventana.get_height() - self.radio
        limite_x = self.ventana.get_width() - self.radio
        v_x, v_y = self.velocidad
        pos_x, pos_y = self.posicion
        pos_x += v_x
        pos_y += v_y
        if pos_x >= limite_x or pos_x <= self.radio:
            v_x *= -1
        if pos_y >= limite_y or pos_y <= self.radio:
            v_y *= -1
        self.velocidad = [v_x, v_y]
        self.posicion = [pos_x, pos_y]        
    
    def dibujar(self) -> None:
        pygame.draw.circle(self.ventana, self.color, self.posicion, self.radio)

    def colisiona_con(self, particula: Particula) -> bool:
        x1, y1 = self.posicion
        x2, y2 = particula.posicion
        distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        return distancia < (self.radio * 2)

    def manejar_colision(self, otra_particula: Particula) -> None:
        dx = otra_particula.posicion[0] - self.posicion[0]
        dy = otra_particula.posicion[1] - self.posicion[1]
        distancia = math.sqrt(dx**2 + dy**2)
        dx /= distancia
        dy /= distancia
        self.velocidad = (self.velocidad[0] - dx, self.velocidad[1] -  dy)
        otra_particula.velocidad = (otra_particula.velocidad[0] +  dx, 
                                otra_particula.velocidad[1] + dy)
            
if __name__ == '__main__':
    pygame.init()

    #parametros base
    fullscreen = False
    color_ventana = pygame.Color(0,0,0)
    radio = 10
    velocidad_base = (2, 2)
    num_particulas = int(input("Cantidad de particulas: "))

    #ventana
    ventana = pygame.display.set_mode((1200,675))
    pygame.display.set_caption("test colisionador")
    ventana.fill(color_ventana)

    #particulas
    pos_iniciales = []
    colores = []
    particulas = []
    for i in range(num_particulas):
        pos_inicial = (randint(radio, ventana.get_width() - radio), 
                    randint(radio, ventana.get_height() - radio))
        while pos_inicial in pos_iniciales:
            pos_inicial = (randint(radio, ventana.get_width() - radio), 
                    randint(radio, ventana.get_height() - radio))
        color = (randint(0,255), randint(0,255), randint(0,255))
        while color in colores:
            color = (randint(0,255), randint(0,255), randint(0,255))
        velocidad = map(lambda x: x * -1 if randint(0, 1) == 1 else x  , velocidad_base)
        particulas.append(Particula(ventana, color, pos_inicial, radio, velocidad))


    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F11:
                    fullscreen = not fullscreen
                    if fullscreen:
                        ventana = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
                    else:
                        ventana = pygame.display.set_mode((1200, 675))
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()
        
        ventana.fill(color_ventana)
        
        for particula in particulas:
            particula.avanzar()
            particula.dibujar()
        for i in range(len(particulas)):
            for j in range(i + 1, len(particulas)):
                if particulas[i].colisiona_con(particulas[j]):
                    particulas[i].manejar_colision(particulas[j])

        pygame.display.update()
    



        