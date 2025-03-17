import circleshape
import pygame
from constants import *


class Shot(circleshape.CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
    
    def draw(self, screen):
        return pygame.draw.circle(
            screen, pygame.Color("white"), self.position, self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt

    def set_velocity(self, vel_vect):
        self.velocity = vel_vect
