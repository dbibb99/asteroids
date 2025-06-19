import pygame
from constants import *
from player import Player

pygame.init()


def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    color = (0,0,0)

    game_clock = pygame.time.Clock()
    dt = 0

    game_running = True

    new_player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while game_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(color)
        new_player.draw(screen=screen)
        pygame.display.flip()
        game_running = True
        dt = game_clock.tick(60) / 1000    
        
if __name__ == "__main__":
    main()

