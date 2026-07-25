import Universe 
from Tile import Tile 
import pygame 
import random 
from LayerTypeIs import LayerTypeIs
# import LandscapeCA

class Gameboard:
    def __init__(self, rows = 100, cols = 100):
        self.rows = rows 
        self.cols = cols 
        self.board = [[Tile() for i in range(cols)] for j in range(rows)]
        #Since boards are square, measure this one way, and you've got it for both ways 
        self.BOARD_SIZE = rows * self.board[0][0].square_dimesion_px
        self.gameworld = None 

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
        #print("FIRST RENDERED IS " +str(row_lower_bound)+ " , " +str(column_lower_bound))
        for j in range(column_lower_bound, column_upper_bound):
            for i in range(row_lower_bound, row_upper_bound):
                self.board[i][j].render()
                # self.board[i][j].refreshExternal()
                current_board_surface.blit(self.board[i][j].image, (row_count*50, col_count*50))
                if self.board[i][j].stood_on == True:
                    current_board_surface.blit(self.board[i][j].stood_on_by.surface_sprite, (row_count*50, col_count*50))
                else:
                    pass 
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

        for person in Universe.persons_dict.keys():
            #print(Universe.persons_dict[person])
            rand_roll = int(random.uniform(0, 99))
            rand_roll2 = int(random.uniform(0, 99))
            self.board[rand_roll][rand_roll2].render()
            if self.board[rand_roll][rand_roll2].tileWalkable() == True:
                print("it was true!")
                Universe.persons_dict[person].person_pos_x = rand_roll
                Universe.persons_dict[person].person_pos_y = rand_roll2
                self.board[rand_roll][rand_roll2].stood_on = True
                self.board[rand_roll][rand_roll2].stood_on_by = Universe.persons_dict[person]
            else:
                pass   

        #print("AT START [24][48]: " +str(self.board[24][48].external))

        
    def generatePlainsBoard(self):
        
        ##SHARED LAYER OF VERY DEEP DIRT  HOLE 
        for j in range(self.cols):
            for i in range(self.rows):
                self.board[i][j].layers.append(LayerTypeIs.DIRT_HOLE_VERY_DEEP)
        

        
        
        pass

    def generateWoodedBoard(self):
        pass

    def generateLakelandsBoard(self):
        #self.gameworld = LandscapeCA.make_landscape()
        
        # for j in range(0, 100):
        #     for i in range(0, 100):
        #         pass 
        pass 
    
    
    
    def generateCoastalBoard(self):
        pass

    def generateTestBoard(self):
        for j in range(0, 100):
            for i in range(0, 100):
                self.board[i][j].addTileLayer(LayerTypeIs.OCEAN_VERY_DEEP)

        for j in range(24, 49):
            for i in range(24, 49):
                self.board[i][j].addTileLayer(LayerTypeIs.LAKE_SHALLOW)
                

        for j in range(49, 74):
            for i in range(49, 74):
                self.board[i][j].addTileLayer(LayerTypeIs.SHORT_GRASS)
                
        
        for j in range(74, 100):
            for i in range(74, 100):
                self.board[i][j].addTileLayer(LayerTypeIs.OCEAN_SHALLOW)

        for person in Universe.persons_dict.keys():
            #print(Universe.persons_dict[person])
            rand_roll = int(random.uniform(0, 99))
            rand_roll2 = int(random.uniform(0, 99))
            self.board[rand_roll][rand_roll2].render()
            if self.board[rand_roll][rand_roll2].tileWalkable() == True:
                #print("it was true!")
                Universe.persons_dict[person].person_pos_x = rand_roll
                Universe.persons_dict[person].person_pos_y = rand_roll2
                self.board[rand_roll][rand_roll2].stood_on = True
                self.board[rand_roll][rand_roll2].stood_on_by = Universe.persons_dict[person]
            else:
                pass   

    def IliumCrossing(self):
        for j in range(0, 100):
            for i in range(0, 100):
                self.board[i][j].addTileLayer(LayerTypeIs.SHORT_GRASS) 





        ## ============= BORDERS  
        for k in range(0, 100):
            self.board[0][k].addTileLayer(LayerTypeIs.BEDROCK)
            pass
        
        for m in range(0, 100):
            self.board[m][0].addTileLayer(LayerTypeIs.BEDROCK)

        for i in range(0, 100):
            self.board[99][i].addTileLayer(LayerTypeIs.BEDROCK)
        
        for i in range(0, 100):
            self.board[i][99].addTileLayer(LayerTypeIs.BEDROCK)

        ## ============






        # for j in range(0, 100):
        #     for i in range(0, 100):
        #         self.board[i][j].addTileLayer(LayerTypeIs.FOG)




        pass 
    
