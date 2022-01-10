import pygame
import os
import numpy as np
from random import randint

WIDTH, HEIGHT = 355, 355
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Minesweeper Clone")

BG_COLOUR = (120, 120, 120)
CELL_COLOUR = (170, 170, 170)

FPS = 60
CELL_WIDTH, CELL_HEIGHT = 30, 30
MARGIN = 5

#draws the inital game board
def draw_window(gamemode):
    for row in range(gamemode):
        for col in range(gamemode):
            colour = CELL_COLOUR
            pygame.draw.rect(WIN, colour, [(MARGIN+CELL_WIDTH)*col + MARGIN, 
                            (MARGIN+CELL_HEIGHT)*row + MARGIN, CELL_WIDTH, CELL_HEIGHT])
    pygame.display.update()

#places bombs at random spots
def place_bombs(gamemode, board):
    num_bombs = 10
    for bombs in range(num_bombs):
        ybomb = randint(0, gamemode-1)
        xbomb = randint(0, gamemode-1)
        while board[ybomb, xbomb] == 10:
            ybomb = randint(0, gamemode-1)
            xbomb = randint(0, gamemode-1)
        board[ybomb, xbomb] = 10
        print(ybomb, " ", xbomb)

#updates the board based on the chosen cell
def update_board(board, col, row):
    if board[row, col] == 10:
        colour = (255,255,255)
        print ("bomb")
    else:
        colour = (0, 255, 0)
        print ("no bomb")
    print (col, " ", row)
    pygame.draw.rect(WIN, colour, [(MARGIN+CELL_WIDTH)*col + MARGIN, 
                    (MARGIN+CELL_HEIGHT)*row + MARGIN, CELL_WIDTH, CELL_HEIGHT])
    pygame.display.update()

def main():
    clock = pygame.time.Clock()
    run = True
    newGame = True
    gamemode = 10
    board = np.zeros((gamemode, gamemode))
    col = 0
    row = 0
    while run:
        clock.tick(FPS)

        if newGame:
            place_bombs(gamemode, board)
            draw_window(gamemode)
            print(board)
            newGame = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                position = pygame.mouse.get_pos()
                col = position[0] // (MARGIN + CELL_WIDTH)
                row = position[1] // (MARGIN + CELL_HEIGHT)
                update_board(board, col, row)
    
    pygame.quit()

if __name__ == "__main__":
    main()