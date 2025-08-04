import pygame
from constants import *

def main():
    pygame.init() # Initialize Pygame
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # Set the screen size
    clock = pygame.time.Clock() # Create a clock object
    dt = 0  # Delta time for frame rate control

    # Main game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
    
        screen.fill((0, 0, 0))  # Fill the screen with black
        pygame.display.flip()  # Update the display

        dt = clock.tick(60) / 1000.0  # limit the framerate to 60 FPS

if __name__ == "__main__":
    main()
