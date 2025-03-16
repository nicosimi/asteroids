import pygame
import circleshape
from constants import *

class Asteroid(circleshape.CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        return pygame.draw.circle(
            screen, pygame.Color("white"), self.position, self.radius, width=2)
    
    def update(self, dt):
        self.position += self.velocity * dt