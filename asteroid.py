import pygame
from circleshape import CircleShape
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        color = (250, 250, 250)  # white
        line_width = 2
        pygame.draw.circle(screen, color=color, center=self.position, radius=self.radius, width=line_width)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        radius = self.radius
        velocity = self.velocity
        position = self.position
        self.kill()
        if radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20, 50)
        velocity_one = velocity.rotate(angle)
        velocity_two = velocity.rotate(-angle)
        new_asteroid_one = Asteroid(position.x, position.y, radius= radius - ASTEROID_MIN_RADIUS)
        new_asteroid_one.velocity = velocity_one * 1.2
        new_asteroid_two = Asteroid(position.x, position.y, radius= radius - ASTEROID_MIN_RADIUS)
        new_asteroid_two.velocity = velocity_two
