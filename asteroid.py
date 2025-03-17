import pygame
import circleshape
from constants import *
import random

class Asteroid(circleshape.CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        return pygame.draw.circle(
            screen, pygame.Color("white"), self.position, self.radius, width=2)
    
    def update(self, dt):
        self.position += self.velocity * dt
    
    def collision(self, other):
        return super().collision(other)

    def split(self):
        old_radius = self.radius
        old_position = self.position
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS: return
        ran_val = random.uniform(20,50)
        first_vel = self.velocity.rotate(ran_val)
        second_vel = self.velocity.rotate(-ran_val)
        first_ast = Asteroid(*old_position,old_radius - ASTEROID_MIN_RADIUS)
        second_ast = Asteroid(*old_position, old_radius - ASTEROID_MIN_RADIUS)
        first_ast.velocity = first_vel * 1.2
        second_ast.velocity = second_vel * 1.2
