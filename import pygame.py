import pygame
import sys

WIDTH = 600
HEIGHT = 600
CELL_SIZE = 120
ROWS = 5
COLS = 5
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption('Хрестики-нулики')

board = [['' for _ in range(COLS)] for _ in range(ROWS)]

current_player = 'X'



def draw_board():
    screen.fill(BLACK)
    for row in range(ROWS):
        for col in range(COLS):
            pygame.draw.rect(screen, WHITE, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE), 3)
            font = pygame.font.SysFont(None, 48)
            text = font.render(board[row][col], True, BLUE)
            screen.blit(text, (col * CELL_SIZE + CELL_SIZE // 2 - text.get_width() // 2,
                               row * CELL_SIZE + CELL_SIZE // 2 - text.get_height() // 2))



def switch_player():
    global current_player
    if current_player == 'X':
        current_player = 'O'
    else:
        current_player = 'X'



def player_move(row, col):
    global board, current_player
    if board[row][col] == '':
        board[row][col] = current_player



def check_winner():
    
    for row in range(ROWS):
        if all(board[row][col] == current_player for col in range(COLS)):
            return current_player

    
    for col in range(COLS):
        if all(board[row][col] == current_player for row in range(ROWS)):
            return current_player

    
    if all(board[i][i] == current_player for i in range(ROWS)):
        return current_player

    
    if all(board[i][COLS - 1 - i] == current_player for i in range(ROWS)):
        return current_player
    
    
    
    if all(all(cell != '' for cell in row) for row in board):
        return 'Нічия'
    
    return None

def reset_board():
    global board, current_player
    board = [['' for _ in range(COLS)] for _ in range(ROWS)]
    current_player = 'X'

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONUP:

            row = event.pos[1] // CELL_SIZE
            col = event.pos[0] // CELL_SIZE

            player_move(row, col)

            switch_player()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                reset_board()


    draw_board()
    winner = check_winner()
    if winner or winner == 'Нічия':
        font = pygame.font.SysFont(None, 48)
        if winner == 'Нічия':
            text = font.render('Нічия', True, RED)
        else:
            text = font.render(f'Переміг {winner}!', True, RED)
        screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT + CELL_SIZE // 2 - text.get_height() // 2))
    pygame.display.update()