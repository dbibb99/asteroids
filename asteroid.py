import pygame
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        color = (250, 250, 250)  # white
        line_width = 2
        pygame.draw.circle(screen, color=color, center=self.position, radius=self.radius, width=line_width)

    def update(self, dt):
        self.position += self.velocity * dt

