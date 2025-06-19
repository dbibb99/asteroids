import pygame
from circleshape import CircleShape
from constants import *

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
    
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        color = (250, 250, 250)  # white
        points = self.triangle()
        line_width = 2
        pygame.draw.polygon(screen, color=color, points=points, width=line_width)

    def update(self, dt):
        keys = pygame.key.get_pressed()

        # rotate left if pressing 'a'
        if keys[pygame.K_a]:
            self.rotation -= PLAYER_TURN_SPEED * dt
        # rotate right if pressing 'd'
        if keys[pygame.K_d]:
            self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        keys = pygame.key.get_pressed()
        movement = pygame.Vector2(0,1).rotate(self.rotation)

        # move forward when pressing 'w'
        if keys[pygame.K_w]:
            self.position += movement * PLAYER_SPEED * dt

        # move backward when pressing 's'
        if keys[pygame.K_s]:
            self.position -= movement * PLAYER_SPEED * dt
