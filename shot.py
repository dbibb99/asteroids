import pygame
from circleshape import CircleShape
from constants import *

class Shot(CircleShape):
    def __init__(self, position):
            super().__init__(position.x, position.y, radius=SHOT_RADIUS)
            self.position = position

    def draw(self, screen):
        color = (250, 250, 250)  # white
        line_width = 2
        pygame.draw.circle(screen, color=color, center=self.position, radius=self.radius, width=line_width)

    def update(self, dt):
        self.position += self.velocity * dt



