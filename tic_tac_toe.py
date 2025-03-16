import numpy as np
import pygame

ROWS = 3
COLUMNS = 3
WHITE = (255,255,255)
BLACK = (0, 0, 0)
LINE_COLOR = (0, 0, 0)
WIDTH = 600
HEIGHT = 600
SIZE = (WIDTH, HEIGHT)
CELL_SIZE = WIDTH // ROWS
LINE_WIDTH = 10

def draw_grid():
    for i in range(1, ROWS):
        pygame.draw.line(window, LINE_COLOR, (0, i * CELL_SIZE), (WIDTH, i * CELL_SIZE), LINE_WIDTH)
        pygame.draw.line(window, LINE_COLOR, (i * CELL_SIZE, 0), (i * CELL_SIZE, HEIGHT), LINE_WIDTH)

def draw_marks():
    for row in range(ROWS):
        for col in range(COLUMNS):
            if board[row][col] == 1:
                pygame.draw.line(window, BLACK, 
                                (col * CELL_SIZE + 20, row * CELL_SIZE + 20),
                                ((col + 1) * CELL_SIZE - 20, (row + 1) * CELL_SIZE - 20),
                                10)
                pygame.draw.line(window, BLACK, 
                                ((col + 1) * CELL_SIZE - 20, row * CELL_SIZE + 20),
                                (col * CELL_SIZE + 20, (row + 1) * CELL_SIZE - 20),
                                10)
            elif board[row][col] == 2:
                pygame.draw.circle(window, BLACK, 
                                   (col * CELL_SIZE + CELL_SIZE // 2, row * CELL_SIZE + CELL_SIZE // 2),
                                   CELL_SIZE // 3, 10)

def mark(row, col, player):
    board[row][col] = player

def is_valid_mark(row, col):
    return board[row][col] == 0

def is_board_full():
    return not any(0 in row for row in board)

def is_winning_move(player):
    for r in range(ROWS):
        if all(board[r][c] == player for c in range(COLUMNS)):
            return True
    for c in range(COLUMNS):
        if all(board[r][c] == player for r in range(ROWS)):
            return True
    if all(board[i][i] == player for i in range(ROWS)) or all(board[i][ROWS - 1 - i] == player for i in range(ROWS)):
        return True
    return False

board = np.zeros((ROWS,COLUMNS))
game_over = False
Turn = 0

pygame.init()
window = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Tic Tac Toe")
window.fill(WHITE)
draw_grid()
pygame.display.update()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            x, y = event.pos
            row = y // CELL_SIZE
            col = x // CELL_SIZE

            if is_valid_mark(row, col):
                mark(row, col, 1 if Turn % 2 == 0 else 2)
                if is_winning_move(1 if Turn % 2 == 0 else 2):
                    print(f"Player {1 if Turn % 2 == 0 else 2} Wins!")
                    game_over = True
                elif is_board_full():
                    print("It's a Draw!")
                    game_over = True
                Turn += 1

            window.fill(WHITE)
            draw_grid()
            draw_marks()
            pygame.display.update()

pygame.quit()
