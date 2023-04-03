import pygame
from table import *
from config import *

pygame.init()

def draw_table():
    ''' Drawing chess table '''
    for block in table.blocks:
        window.blit(block.image, block.pos)

def game_loop():
    ''' Game Loop '''
    global run
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        pygame.display.update()
        clock.tick(FPS)

def main():
    ''' Main function with game loop '''
    draw_table()
    game_loop()
    

''' Create window '''
window = pygame.display.set_mode(WIN_SIZE)
pygame.display.set_caption('Chess')
clock = pygame.time.Clock()
run = True
table = ChessTable(size=WIN_SIZE)



if __name__ == '__main__':
    main()