import circleshape
import pygame
from constants import *

class Player(circleshape.CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
    
    def triangle(self):
        forward = pygame.Vector2(0,1).rotate(self.rotation)
        right = pygame.Vector2(0,1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        unit_v = pygame.Vector2(0,1).rotate(self.rotation)
        speed = PLAYER_SPEED * dt
        unit_v.scale_to_length(float(speed))
        self.position += unit_v


    def draw(self, screen):
        pygame.draw.polygon(screen, pygame.Color("white"), self.triangle(), width=2)

    def update(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]: #rotate left
            self.rotate(0-dt)
        if keys[pygame.K_d]: #rotate right
            self.rotate(dt)
        if keys[pygame.K_w]: #move forward
            self.move(dt)
        if keys[pygame.K_s]: #move backwards
            self.move(0-dt)