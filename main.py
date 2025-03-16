import pygame
from constants import *

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode(
        (SCREEN_WIDTH, SCREEN_HEIGHT)
    )
    game_clock = pygame.time.Clock()
    dt = 0

    while True: #GAMELOOP
        screen.fill("BLACK")
        pygame.display.flip()
        dt = game_clock.tick(60) #frame rate = 60fps, returns time between frames
        dt = dt/1000 #convert to milliseconds to seconds

if __name__ == "__main__":
    main()