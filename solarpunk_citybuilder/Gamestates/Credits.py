from Gamestates.Gamestate import Gamestate
from Gamestates.GamestateIs import GamestateIs
import pygame

class Credits(Gamestate):
    def __init__(self):
        super().__init__()
        self.internal_state = GamestateIs.CREDITS
        self.transition_state = GamestateIs.CREDITS

    def handleKeyInputs(self, keys):
        if keys[pygame.K_RETURN]:
            self.transition_state = GamestateIs.MAIN_MENU
        if keys[pygame.K_ESCAPE]:
            self.transition_state = GamestateIs.MAIN_MENU
    
    def handleMouseInputs(self, mouse):
        return super().handleMouseInputs(mouse)
    
    def drawDisplay(self, display_surface):
        credits_canvas = pygame.Surface((1200, 800)).convert_alpha()
        credits_canvas.fill("green")

        credits_font = pygame.font.Font(None, 48)
        credits_text_font = pygame.font.Font(None, 28)

        title_string = "CREDITS"
        title_surface = credits_font.render(title_string, False, "White")

        credits_body = "Original Concept: Shawn Robinson & Dylan Miley \nLead Programmer & Game Design: Shawn Robinson\nArtwork: Gabriela Robinson\nMusic: Dylan Miley\nWorld Seed Generation: Dylan Miley\n\nSpecial Thanks:\nw3schools.com\npygame-ce\n"

        body_surface = credits_text_font.render(credits_body, False, "Black")

        credits_canvas.blit(title_surface, (600, 400))
        credits_canvas.blit(body_surface, (625, 450))

        display_surface.blit(credits_canvas, (0,0))

        pass

    def getInternalState(self):
        return super().getInternalState()
    
    def Reset(self):
        self.internal_state = GamestateIs.CREDITS
        self.transition_state = GamestateIs.CREDITS
