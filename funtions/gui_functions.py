import pygame
import sys

pygame.init()

# Set up display
width, height = 400, 300
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Mouse Collision Example")

# Create a rectangle
rect = pygame.Rect(50, 50, 100, 50)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Get the mouse position
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Check for collision
    if rect.collidepoint(mouse_x, mouse_y):
        print("Mouse collides with the rectangle!")

    # Draw the rectangle
    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (255, 0, 0), rect)
    pygame.display.flip()
    pygame.time.delay(10)
