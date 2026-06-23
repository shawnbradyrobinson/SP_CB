from Gamestates.Gamestate import Gamestate
from Gamestates.GamestateIs import GamestateIs
import pygame 

class MainMenu(Gamestate):
    def __init__(self):
        super().__init__()
        self.internal_state = GamestateIs.MAIN_MENU
        self.transition_state = GamestateIs.MAIN_MENU
        pass

    def handleKeyInputs(self, keys):
        if keys[pygame.K_RETURN]:
            print("ENTER")
            self.transition_state = GamestateIs.OBSERVING
            pass

    def handleMouseInputs(self, mouse):
        return super().handleMouseInputs(mouse)
    
    def drawDisplay(self, display_surface):
        main_menu_canvas = pygame.Surface((1200, 800)).convert_alpha()
        main_menu_canvas.fill("green")

        main_menu_font = pygame.font.Font(None, 48)
        title_string = "SOLAR PUNK CITY BUILDER"
        title_surface = main_menu_font.render(title_string, False, "White")

        display_surface.blit(main_menu_canvas, (0,0))
        display_surface.blit(title_surface, (600, 400))


        pass

    def getInternalState(self):
        return super().getInternalState()

    def Reset(self):
        self.internal_state = GamestateIs.MAIN_MENU
        self.transition_state = GamestateIs.MAIN_MENU