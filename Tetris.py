import sys
import pygame
import datetime
import math
import pygame.freetype

pygame.init()
GAME_FONT = pygame.freetype.Font("DayDream.ttf", 24)



def ZeroField(n):
    return [[0] * n for i in range(n)]

def BetterZeroField(x, y):
    return [[0] * x for i in range(y)]

def main():
    
    width = 700
    height = 850
    cellSide = 50
    score = 0

    screen = pygame.display.set_mode((width + 200, height))
    running = True
    xIdx = 2
    yIdx = 2
    # board = BetterZeroField(width/cellSide, height/cellSide)
    while running:
        pygame.display.flip()
        screen.fill((0, 0, 0))

        text_surface, rect = GAME_FONT.render("Score:", (255, 0, 0))
        text, rect = GAME_FONT.render(str(score), (255, 0, 0))
        tetris, rect = GAME_FONT.render("TETRIS", (255, 0, 0))
        screen.blit(text_surface, (720, 300))
        screen.blit(tetris, (720, 150))
        screen.blit(text, (720, 340))

        pygame.draw.line(screen, (255, 255, 255), (700, 0), (700, 850), 1)

        pygame.draw.rect(screen, (255, 255, 255), (xIdx * cellSide + 1, yIdx * cellSide + 1, cellSide - 1, cellSide - 1))



        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                running = False
            elif events.type == pygame.KEYDOWN:
                if events.key == pygame.K_LEFT:
                    xIdx -= 1
                    if(xIdx == -1):
                        xIdx = 0
                elif events.key == pygame.K_RIGHT:
                    xIdx += 1
                    if(xIdx == width/cellSide):
                        xIdx = width/cellSide - 1
                elif events.key == pygame.K_UP:
                    yIdx -= 1
                    if(yIdx == -1):
                        yIdx = 0
                elif events.key == pygame.K_DOWN:
                    yIdx += 1
                    if(yIdx == height/cellSide):
                        yIdx = height/cellSide - 1

main()