import pygame
import sys
from funtions import Button

# Constants
WIDTH = HEIGHT = 750
ROWS, COLS = 3, 3
BUTTON_SIZE = 250
BUTTON_MARGIN = 0

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

def make_buttons(buttons):
    for row in range(ROWS):
        for col in range(COLS):
            x = col * (BUTTON_SIZE + BUTTON_MARGIN) + BUTTON_MARGIN
            y = row * (BUTTON_SIZE + BUTTON_MARGIN) + BUTTON_MARGIN
            button = Button(x, y, BUTTON_SIZE, BUTTON_SIZE, BLUE, f"{row}-{col}")
            buttons.append(button)
    return buttons


#Inicialise pygame
pygame.init()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
pygame.quit()
            
            