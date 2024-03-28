import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the window
WIDTH, HEIGHT = 750, 750
WINDOW_SIZE = (WIDTH, HEIGHT)
SCREEN = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Tic Tac Toe")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Constants
GRID_SIZE = 3
CELL_SIZE = WIDTH // GRID_SIZE

# Fonts
FONT_SIZE = 60
FONT = pygame.font.SysFont(None, FONT_SIZE)


def draw_grid():
    for i in range(1, GRID_SIZE):
        pygame.draw.line(SCREEN, BLACK, (0, i * CELL_SIZE), (WIDTH, i * CELL_SIZE))
        pygame.draw.line(SCREEN, BLACK, (i * CELL_SIZE, 0), (i * CELL_SIZE, HEIGHT))


def draw_X(row, col):
    x_pos = col * CELL_SIZE + CELL_SIZE // 2
    y_pos = row * CELL_SIZE + CELL_SIZE // 2

    offset = CELL_SIZE // 4

    pygame.draw.line(SCREEN, RED, (x_pos - offset, y_pos - offset), (x_pos + offset, y_pos + offset), 3)
    pygame.draw.line(SCREEN, RED, (x_pos - offset, y_pos + offset), (x_pos + offset, y_pos - offset), 3)


def draw_O(row, col):
    x_pos = col * CELL_SIZE + CELL_SIZE // 2
    y_pos = row * CELL_SIZE + CELL_SIZE // 2
    radius = CELL_SIZE // 4

    pygame.draw.circle(SCREEN, BLACK, (x_pos, y_pos), radius, 3)


def draw_board(board):
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            if board[row][col] == 'X':
                draw_X(row, col)
            elif board[row][col] == 'O':
                draw_O(row, col)


def check_win(board, player):
    for row in range(GRID_SIZE):
        if all([board[row][col] == player for col in range(GRID_SIZE)]):
            return True

    for col in range(GRID_SIZE):
        if all([board[row][col] == player for row in range(GRID_SIZE)]):
            return True

    if all([board[i][i] == player for i in range(GRID_SIZE)]) or \
       all([board[i][GRID_SIZE - i - 1] == player for i in range(GRID_SIZE)]):
        return True

    return False


def main():
    board = [['' for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
    current_player = 'X'
    game_over = False

    while True:
        SCREEN.fill(WHITE)
        draw_grid()
        draw_board(board)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if not game_over and event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                row = y // CELL_SIZE
                col = x // CELL_SIZE

                if board[row][col] == '':
                    board[row][col] = current_player
                    if check_win(board, current_player):
                        print(current_player + " wins!")
                        game_over = True
                    elif all([cell != '' for row in board for cell in row]):
                        print("It's a tie!")
                        game_over = True
                    current_player = 'O' if current_player == 'X' else 'X'

        pygame.display.update()