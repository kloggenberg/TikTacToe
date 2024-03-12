import pygame
import sys
from button_class import Button

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 750, 750
GRID_SIZE = 3
BUTTON_SIZE = WIDTH // GRID_SIZE

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create a window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tik-Tac-Toe")

#List of rects
rects = []

# Function to draw buttons
def make_buttons(rects):
    name = 1
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            x = col * BUTTON_SIZE
            y = row * BUTTON_SIZE
            rect = Button(x,y,BUTTON_SIZE,BUTTON_SIZE,name)
            rects.append(rect)
            name += 1
    return rects

rects = make_buttons(rects)


# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    # Clear the screen
    screen.fill(WHITE)

    #Draw rects
    mouse_x , mouse_y = pygame.mouse.get_pos()
    for rect in rects:
        rect.draw_rect(screen,mouse_x,mouse_y)
        
    # Check for mouse click
    mouse_click = pygame.mouse.get_pressed()
    if mouse_click[0]:  # Left  mouse button clicked
        for rect in rects:
            rect.check_click(mouse_x,mouse_y)
            print(rect.state)
            
        
    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()
sys.exit()