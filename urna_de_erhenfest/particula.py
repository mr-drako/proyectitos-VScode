from __future__ import annotations
import math
import time
import pygame
from random import uniform
from parametros import LIMIT
from collections import defaultdict


class Particula:

    num = 1

    def __init__(self, ventana: pygame.surface.Surface,
                 color: pygame.color.Color, posicion: tuple,
                 radio: int, velocidad: tuple, lado: int):
        self.ventana = ventana
        self.color = color
        self.radio = radio
        self.particula = pygame.draw.circle(ventana, color, posicion, radio)
        self._velocidad = list(velocidad)
        self._posicion = list(posicion)
        self.num = Particula.num
        self.lado = lado
        Particula.num += 1

    @property
    def posicion(self) -> list:
        return tuple(self._posicion)

    @posicion.setter
    def posicion(self, nueva_posicion: tuple) -> None:
        ancho = self.ventana.get_width()
        mitad = ancho // 2
        alto = self.ventana.get_height()
        new_x, new_y = nueva_posicion
        # ajuste y
        new_y = max(self.radio, min(new_y, alto - self.radio))

        # ajuste x
        if self.lado == 1:
            new_x = max(self.radio, min(new_x, mitad - self.radio))
        else:
            new_x = max(self.radio + mitad, min(new_x, ancho - self.radio))
        self._posicion = [new_x, new_y]

    def avanzar(self) -> None:
        ancho = self.ventana.get_width()
        mitad = ancho // 2
        alto = self.ventana.get_height()
        x, y = self.posicion
        v_x, v_y = self.velocidad
        x += v_x
        y += v_y

        # rebotes en y
        if y <= self.radio or y >= alto - self.radio:
            v_y *= -1

        # rebotes en x
        if self.lado == 1:
            if x <= self.radio or x >= mitad - self.radio:
                v_x *= -1
        else:
            if x <= mitad + self.radio or x >= ancho - self.radio:
                v_x *= -1
        self.velocidad = [v_x, v_y]
        self.posicion = [x, y]

    @property
    def velocidad(self) -> list:
        return self._velocidad

    @velocidad.setter
    def velocidad(self, velocidad: list) -> None:
        v_x, v_y = velocidad

        if v_x < 0:
            v_x = max(v_x, -LIMIT)
        else:
            v_x = min(v_x, LIMIT)

        if v_y < 0:
            v_y = max(v_y, -LIMIT)
        else:
            v_y = min(v_y, LIMIT)
        self._velocidad = [v_x, v_y]

    def dibujar(self) -> None:
        pygame.draw.circle(self.ventana, self.color, self.posicion, self.radio)

    def colisiona_con(self, particula: Particula) -> bool:
        x1, y1 = self.posicion
        x2, y2 = particula.posicion
        distancia = (x2 - x1) ** 2 + (y2 - y1) ** 2
        return distancia <= (self.radio * 2) ** 2

    def manejar_colision(self, otra_particula: Particula):
        dx = otra_particula.posicion[0] - self.posicion[0]
        dy = otra_particula.posicion[1] - self.posicion[1]
        distancia = math.sqrt(dx**2 + dy**2)
        try:
            dx /= distancia
            dy /= distancia
        except ZeroDivisionError:
            return
        self.velocidad = (self.velocidad[0] - dx, self.velocidad[1] - dy)
        otra_particula.velocidad = (otra_particula.velocidad[0] + dx,
                                    otra_particula.velocidad[1] + dy)


class Spatial_hash:
    def __init__(self, cell_size: int):
        self.cell_size = cell_size
        self.malla = defaultdict(list)

    def lugar_malla(self, pos: list | tuple) -> tuple:
        x, y = pos
        return (int(x / self.cell_size), int(y / self.cell_size))

    def agregar(self, objeto: any, pos: list | tuple) -> None:
        lugar = self.lugar_malla(pos)
        self.malla[lugar].append(objeto)

    def cercanos(self, pos: list | tuple) -> tuple:
        x, y = self.lugar_malla(pos)
        cercanos = []
        for i in (-1, 0, 1):
            for j in (-1, 0, 1):
                key = (x + i, y + j)
                cercanos.extend(self.malla[key])
        return cercanos


def matriz_probabilidad(num: int) -> list:
    matriz = [[0 for _ in range(num)] for _ in range(num)]
    matriz[0][1] = 1
    for i in range(1, len(matriz)):
        try:
            matriz[i][i - 1] = i / num
        except IndexError:
            pass
        try:
            matriz[i][i + 1] = (num - i) / num
        except IndexError:
            pass
    return matriz


def cambio(l_izq: list[Particula], l_der: list[Particula]) -> tuple:
    if len(l_der) != len(l_izq):
        matriz = matriz_probabilidad(len(l_izq) + len(l_der))
        print(f"cantidad por lado, izq:{len(l_izq)} - der:{len(l_der)}")
        time.sleep(0.1)
        prob = uniform(0, 1)
        while prob == 0:
            prob = uniform(0, 1)
        if len(l_izq) < len(l_der):
            n = len(l_izq)
            ganar = matriz[n][n + 1]
            if ganar > prob:
                part = l_der.pop(0)
                part.lado = 1
                l_izq.append(part)
            else:
                part = l_izq.pop(0)
                part.lado = 2
                l_der.append(part)

        elif len(l_der) < len(l_izq):
            n = len(l_der)
            ganar = matriz[n][n + 1]
            if ganar > prob:
                part = l_izq.pop(0)
                part.lado = 2
                l_der.append(part)

            else:
                part = l_der.pop(0)
                part.lado = 1
                l_izq.append(part)
    return (l_izq, l_der)


if __name__ == "__main__":
    n_part = int(input("n° particulas: "))
    matriz = matriz_probabilidad(n_part)
    der = ["i" for _ in range(n_part)]
    izq = []
    inicio = time.time()
    while len(der) != len(izq):
        print(f"cantidad por lado, izq:{len(izq)} - der:{len(der)}")
        time.sleep(0.1)
        prob = uniform(0, 1)
        while prob == 0:
            prob = uniform(0, 1)
        if len(izq) < len(der):
            n = len(izq)
            perder = matriz[n][n - 1]
            ganar = matriz[n][n + 1]
            if ganar > prob:
                izq.append(der.pop(0))
            else:
                der.append(izq.pop(0))

        elif len(der) < len(izq):
            n = len(der)
            perder = matriz[n][n - 1]
            ganar = matriz[n][n + 1]
            if ganar > prob:
                der.append(izq.pop(0))
            else:
                izq.append(der.pop(0))
    print(f"cantidad por lado, izq:{len(izq)} - der:{len(der)}")
    print(f"tiempo equilibrio: {inicio - time.time()}")
