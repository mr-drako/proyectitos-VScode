import pygame
import time
from random import randint
from particula import Particula

if __name__ == '__main__':
    pygame.init()

    # parametros base
    fullscreen = False
    color_ventana = pygame.Color(0, 0, 0)
    radio = 10
    velocidad_base = (2, 2)
    num_particulas_1 = int(input("Cantidad de particulas izquierda: "))
    num_particulas_2 = int(input("Cantidad de particulas Derecha: "))
    COLOR_LINEA = pygame.Color(255, 255, 255)

    # ventana
    ventana = pygame.display.set_mode((1200, 675))
    pygame.display.set_caption("test colisionador")
    ventana.fill(color_ventana)
    pygame.draw.line(ventana, COLOR_LINEA, (600, 0), (600, 675), 2)
    pygame.display.flip()

    # particulas
    pos_iniciales = []
    colores = []
    particulas = []
    for i in range(num_particulas_1):
        pos_inicial = (randint(radio, ventana.get_width() - radio),
                       randint(radio, ventana.get_height() - radio))
        while pos_inicial in pos_iniciales:
            pos_inicial = (randint(radio, ventana.get_width() - radio),
                           randint(radio, ventana.get_height() - radio))
        color = (randint(0, 255), randint(0, 255), randint(0, 255))
        while color in colores:
            color = (randint(0, 255), randint(0, 255), randint(0, 255))
        velocidad = map(lambda x: x * -1 if randint(0, 1) == 1 else x,
                        velocidad_base)
        particulas.append(Particula(ventana, color, pos_inicial,
                                    radio, velocidad, 1))
    for i in range(num_particulas_2):
        pos_inicial = (randint(radio, ventana.get_width() - radio),
                       randint(radio, ventana.get_height() - radio))
        while pos_inicial in pos_iniciales:
            pos_inicial = (randint(radio, ventana.get_width() - radio),
                           randint(radio, ventana.get_height() - radio))
        color = (randint(0, 255), randint(0, 255), randint(0, 255))
        while color in colores:
            color = (randint(0, 255), randint(0, 255), randint(0, 255))
        velocidad = map(lambda x: x * -1 if randint(0, 1) == 1 else x,
                        velocidad_base)
        particulas.append(Particula(ventana, color, pos_inicial,
                                    radio, velocidad, 2))

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F11:
                    fullscreen = not fullscreen
                    if fullscreen:
                        ventana = pygame.display.set_mode((0, 0),
                                                          pygame.FULLSCREEN)
                    else:
                        ventana = pygame.display.set_mode((1200, 675))
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()

        ventana.fill(color_ventana)
        pygame.draw.line(ventana, COLOR_LINEA, (600, 0), (600, 675), 2)

        for particula in particulas:
            particula.avanzar()
            particula.dibujar()
        for i in range(len(particulas)):
            for j in range(i + 1, len(particulas)):
                if particulas[i].colisiona_con(particulas[j]):
                    particulas[i].manejar_colision(particulas[j])

        pygame.display.update()
        time.sleep(0.001)
