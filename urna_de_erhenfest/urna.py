import parametros as p
import pygame
import time
import threading
from random import randint
from particula import Particula, Spatial_hash, cambio


def urna(parts: tuple) -> None:
    pygame.init()

    n_izq, n_der = parts
    fullscreen = p.FULLSCREEN

    # ventana
    ventana = pygame.display.set_mode((p.WIDTH, p.HEIGHT))
    pygame.display.set_caption("test colisionador")

    # particulas
    pos_iniciales = []
    colores = []
    particulas = []
    izq = []
    der = []

    for _ in range(n_izq):
        pos_inicial = (randint(p.RADIO, p.HALF - p.RADIO),
                       randint(p.RADIO, p.HEIGHT - p.RADIO))
        while pos_inicial in pos_iniciales:
            pos_inicial = (randint(p.RADIO, p.HALF - p.RADIO),
                           randint(p.RADIO, p.HEIGHT - p.RADIO))
        color = (randint(0, 255), randint(0, 255), randint(0, 255))
        while color in colores:
            color = (randint(0, 255), randint(0, 255), randint(0, 255))
        velocidad = (randint(-2, 2) or 1, randint(-2, 2) or 1)
        particula = Particula(ventana, color, pos_inicial,
                              p.RADIO, velocidad, 1)
        particulas.append(particula)
        izq.append(particula)
    for _ in range(n_der):
        pos_inicial = (randint(p.HALF + p.RADIO, p.WIDTH - p.RADIO),
                       randint(p.RADIO, p.HEIGHT - p.RADIO))
        while pos_inicial in pos_iniciales:
            pos_inicial = (randint(p.RADIO, ventana.get_width() - p.RADIO),
                           randint(p.RADIO, ventana.get_height() - p.RADIO))
        color = (randint(0, 255), randint(0, 255), randint(0, 255))
        while color in colores:
            color = (randint(0, 255), randint(0, 255), randint(0, 255))
        velocidad = (randint(-2, 2) or 1, randint(-2, 2) or 1)
        particula = Particula(ventana, color, pos_inicial,
                              p.RADIO, velocidad, 1)
        particulas.append(particula)
        der.append(particula)
    contador = -1
    try:
        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_F11:
                        fullscreen = not fullscreen
                        if fullscreen:
                            ventana = pygame.display.set_mode(
                                (0, 0),
                                pygame.FULLSCREEN)
                        else:
                            ventana = pygame.display.set_mode((1200, 675))
                    elif event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        exit()

            ventana.fill(p.WINDOW_COLOR)
            pygame.draw.line(ventana, p.LINE_COLOR,
                             (ventana.get_width() // 2, 0),
                             (ventana.get_width() // 2,
                              ventana.get_height()), 2)

            contador += 1
            if contador >= p.COUNTER_LIMIT:
                # event_cambio.set()
                thread = threading.Thread(target=cambio, args=(izq, der))
                thread.start()
                contador = 0
            spatio = Spatial_hash(p.CELL_SIZE)
            for particula in particulas:
                particula.avanzar()
                spatio.agregar(particula, particula.posicion)
                particula.dibujar()
            for particula in particulas:
                cercanos = spatio.cercanos(particula.posicion)
                for part in cercanos:
                    if part != particula and particula.colisiona_con(part):
                        particula.manejar_colision(part)
            # texto de cantidad de particulas
            fuente = pygame.font.SysFont('Arial', 36)
            lado_izq = fuente.render(f"cantidad particulas: {len(izq)}", True,
                                     (255, 255, 255))
            lado_der = fuente.render(f"cantidad particulas: {len(der)}", True,
                                     (255, 255, 255))
            ventana.blit(lado_izq, (0, 0))
            ventana.blit(lado_der, (ventana.get_width() // 2, 0))
            pygame.display.flip()
            time.sleep(p.FPS)
    except SystemExit:
        pygame.quit()
