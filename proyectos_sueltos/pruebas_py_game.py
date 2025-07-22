import pygame
from pygame.math import Vector2

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# Coordenadas en diferentes formatos
circle_pos_tuple = (400, 300)
circle_pos_list = [400, 300]
circle_pos_vec = Vector2(400, 300)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Mueve la posición en lista y Vector2
    circle_pos_list[0] += 1
    circle_pos_vec.y += 0.5
    
    # Dibuja círculos (todos funcionan)
    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, (255, 0, 0), circle_pos_tuple, 50)  # Tupla
    pygame.draw.circle(screen, (0, 255, 0), circle_pos_list, 30)    # Lista
    pygame.draw.circle(screen, (0, 0, 255), circle_pos_vec, 20)     # Vector2
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()