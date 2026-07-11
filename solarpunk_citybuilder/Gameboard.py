import Universe 
from Tile import Tile 
import pygame 
import random 
from LayerTypeIs import LayerTypeIs


class Gameboard:
    def __init__(self, rows = 100, cols = 100):
        self.rows = rows 
        self.cols = cols 
        self.board = [[Tile() for i in range(cols)] for j in range(rows)]
        #Since boards are square, measure this one way, and you've got it for both ways 
        self.BOARD_SIZE = rows * self.board[0][0].square_dimesion_px
        pass
    pass

    def printBoard(self):
        print(self.board)

    def drawCurrentBoard(self, start_x, end_x, start_y, end_y) -> pygame.Surface:
        
        column_lower_bound = int(start_y / 50) 
        column_upper_bound = int(end_y / 50)
        row_lower_bound = int (start_x / 50)
        row_upper_bound = int(end_x / 50)

        row_count = 0
        col_count = 0 

        current_board_surface = pygame.Surface((1200, 800)).convert_alpha()
        print("FIRST RENDERED IS " +str(row_lower_bound)+ " , " +str(column_lower_bound))
        for j in range(column_lower_bound, column_upper_bound):
            for i in range(row_lower_bound, row_upper_bound):
                self.board[i][j].render()
                # self.board[i][j].refreshExternal()
                current_board_surface.blit(self.board[i][j].image, (row_count*50, col_count*50))
                row_count = row_count + 1
            col_count = col_count + 1 
            row_count = 0 
        return current_board_surface
    



    def randomBoard(self):
        for j in range(self.cols):
            for i in range(self.rows):
                rand_roll = int(random.uniform(0, 4))
                if rand_roll == 0:
                    self.board[i][j].layers.append(LayerTypeIs.LAKE_SHALLOW)
                    self.board[i][j].refreshExternal()
                elif rand_roll == 1:
                    self.board[i][j].layers.append(LayerTypeIs.SHORT_GRASS)
                    self.board[i][j].refreshExternal()
                elif rand_roll == 2:
                    self.board[i][j].layers.append(LayerTypeIs.BEDROCK)
                    self.board[i][j].refreshExternal()
                elif rand_roll == 3:
                    self.board[i][j].layers.append(LayerTypeIs.TALL_GRASS)
                    self.board[i][j].refreshExternal()
                else:
                    print("did you screw up your rand roll, mate?")

        print("AT START [24][48]: " +str(self.board[24][48].external))

        
    def generatePlainsBoard(self):
        for j in range(self.cols):
            for i in range(self.rows):
                self.board[i][j].layers.append(LayerTypeIs.DIRT_HOLE_VERY_DEEP)
        
        
        
        pass

    def generateWoodedBoard(self):
        pass

    def generateLakelandsBoard(self):
        pass

    def generateCoastalBoard(self):
        pass
