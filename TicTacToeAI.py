import sys
import pygame
import numpy as np

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
grey = (180, 180, 180)
red = (255, 0, 0)
green = (0, 255, 0)

width, height = 300, 300
line_width = 5
board_rows = 3
board_cols = 3
square_size = width // 3
circle_radius = square_size // 3
cross_width = 25
circle_width = 15

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Tic Tac Toe AI")
screen.fill(black)
board = np.zeros((board_rows, board_cols))

def draw_line(color=white):
    for i in range(1, board_rows):
        pygame.draw.line(screen, color, (0, i * square_size), (width, i * square_size))
        pygame.draw.line(screen, color, (i * square_size, 0), (i * square_size, height))

def draw_figures(color=white):
    for row in range(board_rows):
        for col in range(board_cols):
            if board[row][col] == 1:
                pygame.draw.circle(screen, color, (int(col * square_size + square_size // 2), int(row * square_size + square_size // 2)), circle_radius, circle_width)
            elif board[row][col] == 2:
                pygame.draw.line(screen, color, (col * square_size + square_size // 4, row * square_size + square_size // 4), (col * square_size + 3 * square_size // 4, row * square_size + 3 * square_size // 4))
                pygame.draw.line(screen, color, (col * square_size + square_size // 4, row * square_size + 3 * square_size // 4), (col * square_size + 3 * square_size // 4, row * square_size + square_size // 4))

def mark_square(row, col, player):
    board[row][col] = player

def available_square(row, col):
    return board[row][col] == 0

def is_board_full(check_board = board):
    for row in range(board_rows):
        for col in range(board_cols):
            if check_board[row][col] == 0:
                return False
    return True

def check_win(player, check_board=board) :
    for col in range (board_cols) :
        if check_board[0][col] == player and check_board[1][col] == player and check_board[2][col] == player:
            return True
    
    for row in range (board_rows) :
        if check_board[row][0] == player and check_board[row][1] == player and check_board[row][2] == player:
            return True
        
    if check_board[0][0] == player and check_board[1][1] == player and check_board[2][2] == player:
        return True
    
    if check_board[0][2] == player and check_board[1][1] == player and check_board[2][0] == player:
        return True
    
    return False

def minimax(minimax_board, depth, is_maximizing):
    if check_win(2, minimax_board):
        return float('inf')
    if check_win(1, minimax_board):
        return float('-inf')
    elif is_board_full(minimax_board):
        return 0
    
    if is_maximizing:
        best_score = -1000
        for row in range(board_rows):
            for col in range(board_cols):
                if minimax_board[row][col] == 0:
                    minimax_board[row][col] = 2
                    score = minimax(minimax_board, depth + 1, False)
                    minimax_board[row][col] = 0
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = 1000
        for row in range(board_rows):
            for col in range(board_cols):
                if minimax_board[row][col] == 0:
                    minimax_board[row][col] = 1
                    score = minimax(minimax_board, depth + 1, True)
                    minimax_board[row][col] = 0
                    best_score = min(score, best_score)
        return best_score
    
def best_move():
    best_score = 1000
    move = (-1, -1)
    for row in range(board_rows):
        for col in range(board_cols):
            if board[row][col] == 0:
                board[row][col] = 2
                score = minimax(board, 0, False)
                board[row][col] = 0
                if score > best_score:
                    best_score = score
                    move = (row, col)
    if move != (-1, -1):
        mark_square(move[0], move[1], 2)
        return True
    return False

def reset_game():
    screen.fill(black)
    draw_line(white)
    for row in range(board_rows):
        for col in range(board_cols):
            board[row][col] = 0 

draw_line()
player = 1
game_over = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit() 

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouseX = event.pos[0] // square_size
            mouseY = event.pos[1] // square_size

            if available_square(mouseY, mouseX):
                mark_square(mouseY, mouseX, player)
                if check_win(player):
                    game_over = True
                player = player % 2 + 1

                if not game_over :
                    if best_move():
                        if check_win(2):
                            game_over = True
                        player = player % 2 + 1

                if not game_over :
                    if is_board_full():
                        game_over = True
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                reset_game()
                game_over = False
                player = 1

    if not game_over:
        draw_figures()
    else:
        if check_win(1):
            draw_figures(green)
            draw_line(green)
        elif check_win(2):
            draw_figures(red)
            draw_line(red)
        else:
            draw_line(grey)
            draw_figures(grey)


    pygame.display.update()