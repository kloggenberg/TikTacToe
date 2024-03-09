import pygame
import sys
from button_class import Button

# Constants
WIDTH = HEIGHT = 750
ROWS, COLS = 3, 3
BUTTON_SIZE = 250
BUTTON_MARGIN = 0

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

def make_buttons():
    buttons = []
    for row in range(ROWS):
        for col in range(COLS):
            x = col * (BUTTON_SIZE + BUTTON_MARGIN) + BUTTON_MARGIN
            y = row * (BUTTON_SIZE + BUTTON_MARGIN) + BUTTON_MARGIN
            button = Button(x, y, BUTTON_SIZE, BUTTON_SIZE, BLUE, f"{row}-{col}")
            buttons.append(button)
    return buttons


def main():
    # Initialize Pygame
    pygame.init()

    # Create the window
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Button Grid")

    # Create buttons
    buttons = make_buttons()

    # Main game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    for button in buttons:
                        if button.rect.collidepoint(event.pos):
                            print(f"Button clicked: {button.text}")

        # Draw the buttons
        window.fill(WHITE)
        for button in buttons:
            button.draw_unclicked(window)
            # button.draw_clicked(window)

        pygame.display.update()
        
        
if __name__ == "__main__":
    main()
