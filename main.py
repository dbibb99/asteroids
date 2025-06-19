import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

pygame.init()


def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    color = (0,0,0)

    game_clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)

    game_running = True

    new_player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    new_asteroidfield = AsteroidField()

    while game_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(color)
        updatable.update(dt)
        new_player.move(dt)
        for item in drawable:
            item.draw(screen=screen)
        pygame.display.flip()
        game_running = True
        dt = game_clock.tick(60) / 1000    

if __name__ == "__main__":
    main()

