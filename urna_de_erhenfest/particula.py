from __future__ import annotations
import math
import pygame


class Particula:

    num = 1

    def __init__(self, ventana: pygame.surface.Surface,
                 color: pygame.color.Color, posicion: tuple,
                 radio: int, velocidad: tuple, lado: int):
        self.ventana = ventana
        self.color = color
        self.radio = radio
        self.particula = pygame.draw.circle(ventana, color, posicion, radio)
        self.velocidad = velocidad
        self._posicion = list(posicion)
        self.num = Particula.num
        self.lado = lado
        Particula.num += 1

    @property
    def posicion(self) -> list:
        return tuple(self._posicion)

    @posicion.setter
    def posicion(self, nueva_posicion: tuple) -> None:
        if self.lado == 1:
            ajuste_1 = -(self.ventana.get_width() // 2)
            ajuste_2 = 0
        else:
            ajuste_1 = 0
            ajuste_2 = self.ventana.get_width() // 2
        limite_y = self.ventana.get_height() - self.radio
        limite_x = self.ventana.get_width() - self.radio + ajuste_1
        new_pos_x, new_pos_y = nueva_posicion

        # control limites en x
        if new_pos_x >= limite_x:
            new_pos_x = limite_x - 1
        elif new_pos_x < self.radio +  ajuste_2:
            new_pos_x = self.radio + 1 + ajuste_2

        # control limites en y
        if new_pos_y >= limite_y:
            new_pos_y = limite_y - 1
        elif new_pos_y < self.radio:
            new_pos_y = self.radio + 1

        self._posicion = [new_pos_x, new_pos_y]

    def avanzar(self) -> None:
        if self.lado == 1:
            ajuste_1 = -(self.ventana.get_width() // 2)
            ajuste_2 = 0
        else:
            ajuste_1 = 0
            ajuste_2 = self.ventana.get_width() // 2
        limite_y = self.ventana.get_height() - self.radio
        limite_x = self.ventana.get_width() - self.radio + ajuste_1
        v_x, v_y = self.velocidad
        pos_x, pos_y = self.posicion
        pos_x += v_x
        pos_y += v_y
        if pos_x >= limite_x or pos_x <= self.radio + ajuste_2:
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
        try:
            dx /= distancia
            dy /= distancia
        except ZeroDivisionError:
            pass
        self.velocidad = (self.velocidad[0] - dx, self.velocidad[1] - dy)
        otra_particula.velocidad = (otra_particula.velocidad[0] + dx,
                                    otra_particula.velocidad[1] + dy)
