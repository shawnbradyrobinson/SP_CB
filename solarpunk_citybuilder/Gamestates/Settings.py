from Gamestates.Gamestate import Gamestate
from Gamestates.GamestateIs import GamestateIs
import MusicSystem
import pygame 

class Settings(Gamestate):
    def __init__(self):
        super().__init__()
        self.internal_state = GamestateIs.SETTINGS
        self.transition_state = GamestateIs.SETTINGS
        self.options_list = ["MAIN MENU", "JUKEBOX", "RETURN TO GAME"]
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
                self.transition_state = GamestateIs.MAIN_MENU
            elif self.selected_option == 1:
                self.transition_state = GamestateIs.JUKEBOX
            elif self.selected_option == 2:
                self.transition_state = GamestateIs.OBSERVING
            else:
                return 

    def handleMouseInputs(self, mouse):
        return super().handleMouseInputs(mouse)
    
    def drawDisplay(self, display_surface):
        settings_canvas = pygame.Surface((1200, 800)).convert_alpha()
        settings_canvas.fill("gray")

        settings_font = pygame.font.Font(None, 28)


        main_menu_string = self.options_list[0]
        jukebox_string = self.options_list[1]
        return_string = self.options_list[2]

        if self.selected_option == 0:
            mm_surface = settings_font.render(main_menu_string, False, "White")
        else:
            mm_surface = settings_font.render(main_menu_string, False, "Brown")

        if self.selected_option == 1:
            jb_surface = settings_font.render(jukebox_string, False, "White")
        else:
            jb_surface = settings_font.render(jukebox_string, False, "Brown")

        if self.selected_option == 2:
            rg_surface = settings_font.render(return_string, False, "White")
        else:
            rg_surface = settings_font.render(return_string, False, "Brown")


        settings_canvas.blit(mm_surface, (500, 200))
        settings_canvas.blit(jb_surface, (500, 400))
        settings_canvas.blit(rg_surface, (500, 600))

        display_surface.blit(settings_canvas, (0,0))
    def handleMusic(self):
        return 
    
    def getInternalState(self):
        return super().getInternalState()
    
    def Reset(self):
        self.internal_state = GamestateIs.SETTINGS
        self.transition_state = GamestateIs.SETTINGS