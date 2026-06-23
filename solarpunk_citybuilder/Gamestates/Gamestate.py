import pygame 
from Gamestates.GamestateIs import GamestateIs

class Gamestate:
    def __init__(self):
        self.internal_state = GamestateIs.MAIN_MENU 
        self.transition_state = GamestateIs.MAIN_MENU
        pass

    def handleKeyInputs(self, keys):
        pass

    def handleMouseInputs(self, mouse):
        pass

    def drawDisplay(self):
        pass 

    def getInternalState(self):
        if self.internal_state != self.transition_state:
            return self.transition_state
        else:
            return self.internal_state

    def Reset(self):
        pass 

    




