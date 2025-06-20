import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

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
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)

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
        new_player.shoot(dt)
        for item in drawable:
            item.draw(screen=screen)
        for shot in shots:
            print(f"{type(shot)}")
        pygame.display.flip()
        dt = game_clock.tick(60) / 1000 

        for asteroid in asteroids:
            collision = new_player.collision_check(asteroid)
            if collision:
                game_running = False 
        if game_running == False:
            print("Game Over!")
            sys.exit()  

if __name__ == "__main__":
    main()

