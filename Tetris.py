import sys
import pygame
import datetime
import math
import pygame.freetype
import time
import random

pygame.init()
GAME_FONT = pygame.freetype.Font("DayDream.ttf", 24)



def ZeroField(n):
    return [[0] * n for i in range(n)]

def BetterZeroField(x, y):
    return [[0] * x for i in range(y)]

def FalseField(x, y):
    return [[False] * x for i in range(y)]


def RandomNum():
    x = random.randint(1, 7) 
    return x
        
def DFS(map, x, y, visited):
    visited[y][x] = True
    a = True
    b = True
    c = True
    d = True
    if(y >= 1 and map[y][x] == map[y - 1][x] and visited[y - 1][x] == False):
        DFS(map, x, y - 1, visited)
    if(x >= 1 and map[y][x] == map[y][x - 1] and visited[y][x - 1] == False):
        DFS(map, x - 1, y, visited)
    if(x < len(map[y]) - 1 and map[y][x] == map[y][x + 1] and visited[y][x + 1] == False):
        DFS(map, x + 1, y, visited)
    if(y < len(map) - 1 and map[y][x] == map[y + 1][x] and visited[y + 1][x] == False):
        DFS(map, x, y + 1, visited)



def main():
    
    width = 700
    height = 850
    cellSide = 50
    NumWidth = int(width/cellSide)
    NumHeight = int(height/cellSide)
    score = 0
    block = False
    screen = pygame.display.set_mode((width + 200, height))
    running = True
    xIdx = 2
    yIdx = 2
    delta = 0
    visited = FalseField(NumWidth, NumHeight)
    maxHeight = NumHeight - 1


    falseboard = BetterZeroField(NumWidth, NumHeight)
    board = BetterZeroField(NumWidth, NumHeight)
    # board = [
    #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    #         ]
    while running:
        pygame.display.flip()
        screen.fill((0, 0, 0))

        text_surface, rect = GAME_FONT.render("Score:", (255, 0, 0))
        text, rect = GAME_FONT.render(str(score), (255, 0, 0))
        tetris, rect = GAME_FONT.render("TETRIS", (255, 0, 0))
        screen.blit(text_surface, (720, 300))
        screen.blit(tetris, (720, 150))
        screen.blit(text, (720, 340))

        pygame.draw.line(screen, (255, 255, 255), (701, 0), (701, 850), 1)
        # pygame.draw.rect(screen, (255, 255, 255), (xIdx * cellSide + 1, yIdx * cellSide + 1, cellSide - 1, cellSide - 1))

            
        for y in range(NumHeight - 1, 0, -1):
            for x in range(NumWidth):
                if(visited[y][x] == True):
                    pygame.draw.rect(screen, (255, 0, 0), (x * cellSide + 1, y * cellSide + 1, cellSide - 1, cellSide - 1), 1)


        for y in range(NumHeight - 1, 0, -1):
            for x in range(NumWidth):
                if(falseboard[y][x] == 1):
                    pygame.draw.rect(screen, (255, 255, 0), (x * cellSide + 1, y * cellSide + 1, cellSide - 1, cellSide - 1))
                if(falseboard[y][x] == 2):
                    pygame.draw.rect(screen, (255, 0, 255), (x * cellSide + 1, y * cellSide + 1, cellSide - 1, cellSide - 1))
                if(board[y][x] == 1):
                    pygame.draw.rect(screen, (255, 255, 0), (x * cellSide + 1, y * cellSide + 1, cellSide - 1, cellSide - 1))
                if(board[y][x] == 2):
                    pygame.draw.rect(screen, (255, 0, 255), (x * cellSide + 1, y * cellSide + 1, cellSide - 1, cellSide - 1))

        for y in range(NumHeight - 1, 0, -1):
            for x in range(NumWidth):
                if(falseboard[y][x] != 0 and y < NumHeight - 1 and x < NumWidth - 1 and falseboard[y + 1][x + delta] == 0  and board[y + 1][x + delta] == 0 and x + delta >= 0 and x + delta <= NumWidth):
                    falseboard[y + 1][x + delta] = falseboard[y][x]
                    falseboard[y][x] = 0
                    visited[y + 1][x + delta] = visited[y][x]
                    visited[y][x] = 0
                    pygame.time.delay(10)

        for y in range(NumHeight - 1):
            for x in range(NumWidth):
                if(falseboard[NumHeight - 1][x] != 0 and visited[NumHeight - 1][x] == True):
                    for y in range(NumHeight - 1, 0, -1):
                        for x in range(NumWidth):
                            if (falseboard[y][x] != 0):
                                board[y][x] = falseboard[y][x]
                    falseboard = BetterZeroField(NumWidth, NumHeight)
                    block = False
                    visited = FalseField(NumWidth, NumHeight)

        # for y in range(NumHeight - 1):
        #     for x in range(NumHeight - 3):
        #         if(board[y + 1][x] != 0):
        #             for y in range(NumHeight - 1, 0, -1):
        #                 for x in range(NumWidth):
        #                     if (falseboard[y][x] != 0):
        #                         board[y][x] = falseboard[y][x]
        #             falseboard = BetterZeroField(NumWidth, NumHeight)
        #             block = False
        #             visited = FalseField(NumWidth, NumHeight)




        # for x in range(NumWidth):
        #     if((falseboard[NumHeight - 1][x] != 0 and visited[NumHeight - 1][x] == True)):

        #         for y in range(NumHeight - 1, 0, -1):
        #             for x in range(NumWidth):
        #                 if(falseboard[y][x] != 0 and y < NumHeight - 1 and x < NumWidth - 1 and falseboard[y + 1][x + delta] == 0  and board[y + 1][x + delta] == 0 and x + delta >= 0 and x + delta <= NumWidth):
        #                     falseboard[y + 1][x + delta] = falseboard[y][x]
        #                     falseboard[y][x] = 0
        #                     visited[y + 1][x + delta] = visited[y][x]
        #                     visited[y][x] = 0
                                




        #     for y in range(NumHeight - 1, 0, -1):
        #         for x in range(NumWidth):
        #             if (falseboard[y][x] != 0):
        #                 board[y][x] = falseboard[y][x]
        #     falseboard = BetterZeroField(NumWidth, NumHeight)
        #     block = False
        #     visited = FalseField(NumWidth, NumHeight)

        #     for y in range(NumHeight - 2, 0, -1):
        #             for x in range(NumWidth):
        #                 if(board[y + 1][x] != 0):
        #                     for y in range(NumHeight - 1, 0, -1):
        #                         for x in range(NumWidth):
        #                             if(falseboard[y][x] != 0 and y < NumHeight - 1 and x < NumWidth - 1 and falseboard[y + 1][x + delta] == 0  and board[y + 1][x + delta] == 0 and x + delta >= 0 and x + delta <= NumWidth):
        #                                 falseboard[y + 1][x + delta] = falseboard[y][x]
        #                                 falseboard[y][x] = 0
        #                                 visited[y + 1][x + delta] = visited[y][x]
        #                                 visited[y][x] = 0
                                        
        #                     for y in range(NumHeight - 1, 0, -1):
        #                         for x in range(NumWidth):
        #                             if (falseboard[y][x] != 0):
        #                                 board[y][x] = falseboard[y][x]
        #                     falseboard = BetterZeroField(NumWidth, NumHeight)
        #                     block = False
        #                     visited = FalseField(NumWidth, NumHeight)




        # This eliminates the lines
        for y in range(NumHeight - 1, 0, -1):
            a = 0
            for x in range(NumWidth - 1):
                if(falseboard[y][x] != 0):
                    a += 1
            if(a >= NumWidth - 1):
                for x in range(NumWidth - 1):
                    falseboard[y][x] = 0
                score += 100

        # for y in range(NumHeight - 1, 0, -1):
        #     for x in range(NumWidth):
        #         if(board[y][x] != 0 and y < NumHeight and board[y][x + delta] == 0):
        #             print("x")
        #             board[y][x] = board[y][x + delta]
        #             board[y][x + delta] = 0

        for y in range(NumHeight - 1, 0, -1):
            for x in range(NumWidth):
                if(falseboard[y][x] != 0):
                    DFS(falseboard, x, y, visited)
                    

        if(block == False):
            print("Block")     
            BLOCK = RandomNum()
            print(BLOCK)
            if (BLOCK == 1):
                falseboard[1][0] = 1
                falseboard[1][1] = 1
                falseboard[2][0] = 1
                falseboard[2][1] = 1
            elif (BLOCK == 2):
                falseboard[1][1] = 1
                falseboard[2][0] = 1
                falseboard[2][1] = 1
                falseboard[2][2] = 1
            elif (BLOCK == 3):
                falseboard[1][1] = 1
                falseboard[1][2] = 1
                falseboard[2][2] = 1
                falseboard[2][3] = 1
            elif (BLOCK == 4):
                falseboard[1][3] = 1
                falseboard[1][2] = 1
                falseboard[2][2] = 1
                falseboard[2][1] = 1
               
            elif (BLOCK == 5):
                falseboard[2][1] = 1
                falseboard[2][2] = 1
                falseboard[2][3] = 1
                falseboard[1][3] = 1
               
            elif (BLOCK == 6):
                falseboard[2][1] = 1
                falseboard[2][2] = 1
                falseboard[2][3] = 1
                falseboard[1][1] = 1
                
            elif (BLOCK == 7):
                falseboard[2][1] = 1
                falseboard[2][2] = 1
                falseboard[2][3] = 1
                falseboard[2][4] = 1
            block = True
            for y in range(NumHeight):
                for x in range(NumWidth):
                    if(falseboard[y][x] != 0):
                        DFS(board, x, y, visited)
                

            

            
               

        




        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                running = False
            elif events.type == pygame.KEYDOWN:
                if events.key == pygame.K_LEFT:
                        if(xIdx > 1):
                            xIdx -= 1
                            



                            delta = -1
                elif events.key == pygame.K_RIGHT:
                        if(xIdx < width/cellSide - 1):
                            xIdx += 1
                            delta = 1
                elif events.key == pygame.K_UP:
                    yIdx -= 1
                    if(yIdx == -1):
                        yIdx = 0
                elif events.key == pygame.K_DOWN:
                    yIdx += 1
                    if(yIdx == height/cellSide):
                        yIdx = height/cellSide - 1
                elif events.key == pygame.K_SPACE:
                    print(visited)
                    board = BetterZeroField(NumWidth, NumHeight)

            elif events.type == pygame.KEYUP:
                if events.key == pygame.K_LEFT:
                    delta = 0

                elif events.key == pygame.K_RIGHT:
                    delta = 0

main()