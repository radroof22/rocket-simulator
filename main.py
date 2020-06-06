import pygame

running = True

background_colour = (255,255,255)
width = 300
height = 200

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Rocket Simulator")
screen.fill(background_colour)


while running:
    screen.fill(background_colour)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
