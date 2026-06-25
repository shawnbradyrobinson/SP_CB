from Gamestates.Gamestate import Gamestate
from Gamestates.GamestateIs import GamestateIs
import pygame 

class NotDone(Gamestate):
    def __init__(self):
        super().__init__()
        self.internal_state = GamestateIs.NOT_DONE
        self.transition_state = GamestateIs.NOT_DONE


    def handleKeyInputs(self, keys):
        if keys[pygame.K_RETURN]:
            self.transition_state = GamestateIs.MAIN_MENU
        if keys[pygame.K_ESCAPE]:
            self.transition_state = GamestateIs.MAIN_MENU

    def drawDisplay(self, display_surface):
        not_done_canvas = pygame.Surface((1200, 800)).convert_alpha()
        not_done_canvas.fill("White")

        not_done_font = pygame.font.Font(None, 52)

        not_done_string = "Feature Unfinished\nBut your curiosity is appreciated!"

        nd_surface = not_done_font.render(not_done_string, False, "Black")

        not_done_canvas.blit(nd_surface, (600, 400))
        display_surface.blit(not_done_canvas, (0,0))


    def getInternalState(self):
        return super().getInternalState()
    
    def Reset(self):
        self.internal_state = GamestateIs.NOT_DONE
        self.transition_state  = GamestateIs.NOT_DONE

