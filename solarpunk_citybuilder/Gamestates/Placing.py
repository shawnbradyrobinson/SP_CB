from Gamestates.Gamestate import Gamestate
from Gamestates.GamestateIs import GamestateIs
from TimeSystem import TimeSystem
import Universe
import pygame

class Placing(Gamestate):
    def __init__(self):
        super().__init__()
        self.internal_state = GamestateIs.PLACING
        self.transition_state = GamestateIs.PLACING
        self.grid_on = True
        
        self.x_line_list_x1 = [0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200]

        self.y_line_list_x1 = [0, 100, 200, 300, 400, 500, 600, 700, 800]
        
        self.x_line_list_x2 = [0, 200, 400, 600, 800, 1000, 1200]

        self.y_line_list_x2 = [0, 200, 400, 600, 800]

        self.x_line_list_x3 = [0, 400, 800, 1200]

        self.y_line_list_x3 = [0, 400, 800]

        self.active_x_list = self.x_line_list_x1
        self.active_y_list = self.y_line_list_x1

        self.highlight_x = 100
        self.highlight_y = 100

        self.x_pos = 0
        self.y_pos = 0



        pass

    def handleKeyInputs(self, keys):

        if keys[pygame.K_RETURN]:
            #construct building at this highlighted location 
            #so...pass in some coordinates from the highlighting or positioning to the 
            #building, so it knows that it now exists in that spot 
            pass

        if keys[pygame.K_RIGHT]:
            if self.x_pos >= len(self.active_x_list) -1:
                self.x_pos = len(self.active_x_list) -1 
                print("X POS -> " +str(self.x_pos))
                print("Y POS -> " +str(self.y_pos))
            else:
                self.x_pos = self.x_pos + 1
                print("X POS -> " +str(self.x_pos))
                print("Y POS -> " +str(self.y_pos))
        if keys[pygame.K_LEFT]:
            if self.x_pos == 0:
                print("X POS -> " +str(self.x_pos))
                print("Y POS -> " +str(self.y_pos))
                return 
            else:
                self.x_pos = self.x_pos - 1
                print("X POS -> " +str(self.x_pos))
                print("Y POS -> " +str(self.y_pos))
                return 

        if keys[pygame.K_DOWN]:
            if self.y_pos >= len(self.active_y_list) -1 :
                self.y_pos == len(self.active_y_list) -1 
                print("X POS -> " +str(self.x_pos))
                print("Y POS -> " +str(self.y_pos))
                return
            else:
                self.y_pos = self.y_pos + 1 
                print("X POS -> " +str(self.x_pos))
                print("Y POS -> " +str(self.y_pos))
                return 

        if keys[pygame.K_UP]:
            if self.y_pos == 0:
                print("X POS -> " +str(self.x_pos))
                print("Y POS -> " +str(self.y_pos))
                return 
            else:
                self.y_pos = self.y_pos - 1 
                return 

        if keys[pygame.K_w]:
            self.active_y_list = self.sortOutGridLists(self.active_y_list, 1)
            if self.highlight_y <= 100:
                self.highlight_y = 100
            else:
                self.highlight_y = self.highlight_y - 100
            pass

        if keys[pygame.K_a]:
            self.active_x_list = self.sortOutGridLists(self.active_x_list, 0)
            if self.highlight_x <= 100:
                self.highlight_x = 100
            else:
                self.highlight_x = self.highlight_x - 100 
            pass

        if keys[pygame.K_s]:
            self.active_y_list = self.sortOutGridLists(self.active_y_list, 1)
            self.highlight_y = self.highlight_y + 100

        if keys[pygame.K_d]:
            self.active_x_list = self.sortOutGridLists(self.active_x_list, 0)
            self.highlight_x = self.highlight_x + 100 
            pass 

        if keys[pygame.K_ESCAPE]:
            self.transition_state = GamestateIs.SETTINGS

    def handleMouseInputs(self, mouse):
        return super().handleMouseInputs(mouse)
    
    def drawDisplay(self, display_surface, observing_surface, TS: TimeSystem):
        display_surface.blit(observing_surface, (0,0))
        
        for i in self.y_line_list_x1:
            pygame.draw.line(display_surface, "Black", (0, 1*i), (1200, 1*i), 1)

        for j in self.x_line_list_x1:
            pygame.draw.line(display_surface, "Black", (1*j, 0),(1*j, 800), 1)

        pygame.draw.rect(display_surface,"light yellow", pygame.Rect((self.active_x_list[self.x_pos], self.active_y_list[self.y_pos]), (self.highlight_x, self.highlight_y)))
    
    def getInternalState(self):
        return super().getInternalState()
    
    def Reset(self):
        self.internal_state = GamestateIs.PLACING
        self.transition_state = GamestateIs.PLACING

    def sortOutGridLists(self, active_list, x_or_y) -> list:
        #a little sloppy, but we'll do x == 0, y == 1
        
        if x_or_y == 0:
            #len gets to be a stand-in for identifying what list we're dealing with 
            if len(active_list) == 13:
                return self.x_line_list_x2
            elif len(active_list) == 7:
                return self.x_line_list_x3
            else:
                print("active list THREE -- x")
                print("ACTUAL --> " +str(len(active_list)))
                return self.x_line_list_x1
            
        elif x_or_y == 1:
            #len gets to be a stand-in for identifying what list we're dealing with 
            if len(active_list) == 9:
                return self.y_line_list_x2
            elif len(active_list) == 5:
                return self.y_line_list_x3
            else:
                print("active list THREE -- y")
                print("ACTUAL --> " +str(len(active_list)))
                return self.y_line_list_x1
        else:
            print("GOT UNEXEPCTED x_or_y value")
            return self.x_line_list_x1
    