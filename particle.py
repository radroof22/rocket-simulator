import pygame
import math

gravity = (0, .02)
drag = 0.999
elasticity = 0.75

class Particle:
    x = 0
    y = 0 
    size = 1
    color = (0, 0, 0)
    speed = .01
    angle = 0
    width = size * 2
    height = size * 2

    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
        self.color = (255, 255, 255)
        self.width = 300
        self.height = 200

    def display(self, screen):      
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.size)

    def move(self):
        
        self.x += math.sin(self.angle) * self.speed
        self.y += math.cos(self.angle) * self.speed
        self.angle, self.speed = addVectors(self.angle, self.speed, gravity[0], gravity[1])
        self.speed *= drag

    def bounce(self):
        print(f"y: {self.y} \t height: {self.height} \t size: {self.size} \tangle: {self.angle} \t speed: {self.speed}")
        if int(self.y) > self.height - self.size:
            self.y = 2 * (self.height - self.size) - self.y
            self.angle = math.pi - self.angle
            self.speed *= elasticity


def addVectors(angle1, length1, angle2, length2):
    
    x = math.sin(angle1) * length1 + math.sin(angle2) * length2
    y = math.cos(angle1)* length1 + math.cos(angle2)* length2
    length = math.hypot(x,y)
    angle = 0.5 * math.pi - math.atan2(y,x)
    return angle, length