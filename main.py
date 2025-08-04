import pygame
from constants import *
from player import Player

def main():
    pygame.init() # Initialize Pygame
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # Set the screen size
    clock = pygame.time.Clock() # Create a clock object
    dt = 0  # Delta time for frame rate control

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)  # Create a player instance

    # Main game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
    
        screen.fill("black")  # Fill the screen with black
        player.draw(screen)
        pygame.display.flip()  # Update the display

        dt = clock.tick(60) / 1000.0  # limit the framerate to 60 FPS

if __name__ == "__main__":
    main()
