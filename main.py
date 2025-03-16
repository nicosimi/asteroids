import pygame
import player
import asteroid
import asteroidfield
from constants import *

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    ###Initial game configs
    screen = pygame.display.set_mode(
        (SCREEN_WIDTH, SCREEN_HEIGHT)
    )
    game_clock = pygame.time.Clock()
    dt = 0
    updatable_group = pygame.sprite.Group()
    drawable_group = pygame.sprite.Group()
    asteroid_group = pygame.sprite.Group()
    player.Player.containers = (updatable_group, drawable_group)
    asteroid.Asteroid.containers = (asteroid_group, updatable_group, drawable_group)
    asteroidfield.AsteroidField.containers = (updatable_group)
    ### Assets(?) creation
    player_model = player.Player(SCREEN_WIDTH/2 , SCREEN_HEIGHT/2)
    field = asteroidfield.AsteroidField()

    ###Gameloop
    while True:
        screen.fill("BLACK")
        for entity in drawable_group:
            entity.draw(screen)
        dt = game_clock.tick(60) #frame rate = 60fps, returns time between frames
        dt = dt/1000 #convert to milliseconds to seconds
        updatable_group.update(dt)
        pygame.display.flip()


if __name__ == "__main__":
    main()