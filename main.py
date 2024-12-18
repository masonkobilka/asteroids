import sys
import pygame
from constants import *
from player import Player, Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField

UPDATABLE_GROUP = pygame.sprite.Group()
DRAWABLE_GROUP = pygame.sprite.Group()
ASTEROIDS_GROUP = pygame.sprite.Group()
SHOTS_GROUP = pygame.sprite.Group()

def main():
    game_introduction()

    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    Player.containers = (UPDATABLE_GROUP, DRAWABLE_GROUP)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    Asteroid.containers = (ASTEROIDS_GROUP, UPDATABLE_GROUP, DRAWABLE_GROUP)
    AsteroidField.containers = (UPDATABLE_GROUP)
    Shot.containers = (SHOTS_GROUP)

    asteroidfield = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill('black')
        for thing in UPDATABLE_GROUP:
            thing.update(dt)
        for thing in DRAWABLE_GROUP:
            thing.draw(screen)
        for asteroid in ASTEROIDS_GROUP:
            if asteroid.check_collision(player):
                print("Game Over")
                sys.exit()
        for shot in SHOTS_GROUP:
            shot.update(dt)
            shot.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000

def game_introduction():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()