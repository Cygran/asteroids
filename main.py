import pygame
import sys
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    color = (000, 000, 000)
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    AsteroidField.containers = (updatables)
    Asteroid.containers = (asteroids, updatables, drawables)
    Player.containers = (updatables, drawables)
    field = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatables.update(dt)
        for asteroid in asteroids:
            if asteroid.collision_logic(player):
                print("Game over!")
                sys.exit()
        screen.fill(color)
        for drawable in drawables:
            drawable.draw(screen)
        pygame.display.flip()
        clock.tick(60)
        dt = clock.get_time() / 1000
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()
