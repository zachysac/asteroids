# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from asteroidfield import AsteroidField
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
from asteroid import Asteroid
updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroid = pygame.sprite.Group()
Player.containers = (updatable, drawable)
Asteroid.containers = (asteroid,updatable,drawable)
AsteroidField.containers = (updatable)

def main():
    pygame.init()
    drawable = Player((SCREEN_WIDTH / 2),(SCREEN_HEIGHT / 2))
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    
    while True:
        screen.fill(color=(0,0,0))

        drawable.draw(screen)
        updatable.update(dt)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        #limit framerate to 60    
        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()