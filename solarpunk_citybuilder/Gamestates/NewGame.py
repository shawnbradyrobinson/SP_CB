from Gamestates.Gamestate import Gamestate
from Gamestates.GamestateIs import GamestateIs
import pygame 
import random 

class NewGame(Gamestate):
    def __init__(self, gameboard):
        super().__init__()
        self.internal_state = GamestateIs.NEW_GAME
        self.transition_state = GamestateIs.NEW_GAME
        self.options_list = ["TESTBOARD", "randtile", "LAKELANDS", "COASTAL", "RANDOM"] #PLAINS, WOODED, LAKELANDS, COASTAL, RANDOM 
        self.selected_option = 0 
        self.world_gen = self.options_list[0]
        self.gameboard = gameboard
        pass

    def handleKeyInputs(self, keys):
        if keys[pygame.K_UP]:
            if self.selected_option == 0:
                self.selected_option = 0
                #self.world_gen = self.options_list[self.selected_option] 
            else: 
                self.selected_option = self.selected_option - 1
            #self.world_gen = self.options_list[self.selected_option] 

        if keys[pygame.K_DOWN]:
            if self.selected_option == len(self.options_list) -1:
                self.selected_option = len(self.options_list) - 1
                #self.world_gen = self.options_list[self.selected_option] 
            else:
                self.selected_option = self.selected_option + 1 
                #self.world_gen = self.options_list[self.selected_option] 

        if keys[pygame.K_RETURN]:
            if self.selected_option == 0:
                self.gameboard.generateTestBoard()
                self.transition_state = GamestateIs.OBSERVING
            elif self.selected_option == 1:
                self.gameboard.randomBoard()
                self.transition_state = GamestateIs.OBSERVING
            elif self.selected_option == 2:
                self.gameboard.generateLakelandsBoard()
                self.transition_state = GamestateIs.OBSERVING
            elif self.selected_option == 3:
                self.gameboard.genereateCoastalBoard()
                self.transition_state = GamestateIs.OBSERVING
            
            
            
            
            elif self.selected_option == 4:
                rand_roll = int (random.uniform(0,4))
                if rand_roll == 0:
                    self.gameboard.generatePlainsBoard()
                    self.transition_state = GamestateIs.OBSERVING
                elif rand_roll == 1:
                    self.gameboard.generateWoodedBoard()
                    self.transition_state = GamestateIs.OBSERVING
                elif rand_roll == 2:
                    self.gameboard.generateLakelandsBoard()
                    self.transition_state = GamestateIs.OBSERVING
                elif rand_roll == 3:
                    self.gameboard.genereateCoastalBoard()
                    self.transition_state = GamestateIs.OBSERVING
                else:
                    print("RANDOM WORLD GEN FAILURE")
                    return 
            else:
                return
    
    def drawDisplay(self, display_surface):
        new_game_canvas = pygame.Surface((1200, 800)).convert_alpha()
        new_game_canvas.fill("green")

        new_game_font = pygame.font.Font(None, 48)
        new_game_option_font = pygame.font.Font(None, 28)

        choose_string = "CHOOSE A WORLD TEMPLATE"
        choose_surface = new_game_font.render(choose_string, False, "White")

        option_zero_string = self.options_list[0]
        option_one_string = self.options_list[1]
        option_two_string = self.options_list[2]
        option_three_string = self.options_list[3]
        option_four_string = self.options_list[4]

        if self.selected_option == 0:
            opz_surface = new_game_option_font.render(option_zero_string, False, "White")
        else:
            opz_surface = new_game_option_font.render(option_zero_string, False, "Black")

        if self.selected_option == 1:
            opone_surface = new_game_option_font.render(option_one_string, False, "White")
        else:
            opone_surface = new_game_option_font.render(option_one_string, False, "Black")

        if self.selected_option == 2:
            optwo_surface = new_game_option_font.render(option_two_string, False, "White")
        else:
            optwo_surface = new_game_option_font.render(option_two_string, False, "Black")

        if self.selected_option == 3:
            opthree_surface = new_game_option_font.render(option_three_string, False, "White")
        else:
            opthree_surface = new_game_option_font.render(option_three_string, False, "Black")

        if self.selected_option == 4:
            opfour_surface = new_game_option_font.render(option_four_string, False, "White")
        else:
            opfour_surface = new_game_option_font.render(option_four_string, False, "Black")

        print(self.selected_option)
        new_game_canvas.blit(choose_surface, (600, 400))
        new_game_canvas.blit(opz_surface, (625, 450))
        new_game_canvas.blit(opone_surface, (625, 500))
        new_game_canvas.blit(optwo_surface, (625, 550))
        new_game_canvas.blit(opthree_surface, (625, 600))
        new_game_canvas.blit(opfour_surface, (625, 650))
        

        display_surface.blit(new_game_canvas, (0,0))

        pass


    def getInternalState(self):
        return super().getInternalState()
    
    def Reset(self):
        self.internal_state = GamestateIs.NEW_GAME
        self.transition_state = GamestateIs.NEW_GAME