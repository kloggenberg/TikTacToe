import pygame

pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("My Pygame Window")

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Game logic goes here

    # Drawing
    screen.fill((255, 255, 255))  # Fill the screen with a white color
    pygame.display.update()

pygame.quit()

