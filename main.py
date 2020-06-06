import pygame
from particle import Particle
import random
import math

running = True
                    # Red Green Blue
background_color = (0, 175, 255)

width = 300
height = 200

clock = pygame.time.Clock()

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Rocket Simulator")

particle = Particle(150, 100, 10)
particle.speed = 20
particle.angle = 0
i = 0
while running == True:
    i += 1
    # if i > 20 : break
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    # Draing
    screen.fill(background_color)
    
    particle.move()
    particle.bounce()
    particle.display(screen)

    pygame.display.update()

    
