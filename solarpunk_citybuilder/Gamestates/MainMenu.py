from Gamestates.Gamestate import Gamestate
from Gamestates.GamestateIs import GamestateIs
import pygame 

class MainMenu(Gamestate):
    def __init__(self):
        super().__init__()
        self.internal_state = GamestateIs.MAIN_MENU
        self.transition_state = GamestateIs.MAIN_MENU
        self.options_list = ["NEW GAME", "LOAD GAME", "RECORDS", "CREDITS"]
        self.selected_option = 0

        pass

    def handleKeyInputs(self, keys):
        if keys[pygame.K_UP]:
            if self.selected_option == 0:
                self.selected_option = 0
            else: 
                self.selected_option = self.selected_option - 1 

        if keys[pygame.K_DOWN]:
            if self.selected_option == len(self.options_list) -1:
                self.selected_option = len(self.options_list) - 1
            else:
                self.selected_option = self.selected_option + 1 

        if keys[pygame.K_RETURN]:
            if self.selected_option == 0:
                self.transition_state = GamestateIs.NEW_GAME
            elif self.selected_option == 1:
                self.transition_state = GamestateIs.NOT_DONE
            elif self.selected_option == 2:
                self.transition_state = GamestateIs.NOT_DONE
            elif self.selected_option == 3:
                self.transition_state = GamestateIs.NOT_DONE
            else:
                return

    def handleMouseInputs(self, mouse):
        return super().handleMouseInputs(mouse)
    
    def drawDisplay(self, display_surface):
        main_menu_canvas = pygame.Surface((1200, 800)).convert_alpha()
        main_menu_canvas.fill("green")

        main_menu_font = pygame.font.Font(None, 48)
        menu_option_font = pygame.font.Font(None, 28)



        title_string = "SOLAR PUNK CITY BUILDER"
        title_surface = main_menu_font.render(title_string, False, "White")

        option_zero_string = self.options_list[0]
        option_one_string = self.options_list[1]
        option_two_string = self.options_list[2]
        option_three_string = self.options_list[3]

        if self.selected_option == 0:
            opz_surface = menu_option_font.render(option_zero_string, False, "White")
        else:
            opz_surface = menu_option_font.render(option_zero_string, False, "Black")

        if self.selected_option == 1:
            opone_surface = menu_option_font.render(option_one_string, False, "White")
        else:
            opone_surface = menu_option_font.render(option_one_string, False, "Black")

        if self.selected_option == 2:
            optwo_surface = menu_option_font.render(option_two_string, False, "White")
        else:
            optwo_surface = menu_option_font.render(option_two_string, False, "Black")

        if self.selected_option == 3:
            opthree_surface = menu_option_font.render(option_three_string, False, "White")
        else:
            opthree_surface = menu_option_font.render(option_three_string, False, "Black")



        main_menu_canvas.blit(title_surface, (600, 400))
        main_menu_canvas.blit(opz_surface, (625, 450))
        main_menu_canvas.blit(opone_surface, (625, 500))
        main_menu_canvas.blit(optwo_surface, (625, 550))
        main_menu_canvas.blit(opthree_surface, (625, 600))



        display_surface.blit(main_menu_canvas, (0,0))


        pass

    def getInternalState(self):
        return super().getInternalState()

    def Reset(self):
        self.internal_state = GamestateIs.MAIN_MENU
        self.transition_state = GamestateIs.MAIN_MENU