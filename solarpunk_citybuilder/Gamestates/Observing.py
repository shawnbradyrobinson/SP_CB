from Gamestates.Gamestate import Gamestate
from Gamestates.GamestateIs import GamestateIs
from TimeSystem import TimeSystem
import MusicSystem
import Universe 
import pygame

class Observing(Gamestate):
    def __init__(self):
        super().__init__()
        self.internal_state = GamestateIs.OBSERVING
        self.transition_state = GamestateIs.OBSERVING
        self.music_started = False 
        pass

    def handleKeyInputs(self, keys, TS: TimeSystem):
        if keys[pygame.K_RIGHT]:
            TS.changeDelta(TS.delta * 2)
                
        if keys[pygame.K_LEFT]:
            TS.changeDelta(TS.delta * .5)

        if keys[pygame.K_DOWN]:
            if TS.delta == 0:
                TS.changeDelta(1)
            else: 
                TS.changeDelta(0)

        if keys[pygame.K_j]:
            self.music_started = False 
            self.transition_state = GamestateIs.JUKEBOX

        if keys[pygame.K_ESCAPE]:
            self.transition_state = GamestateIs.SETTINGS

        if keys[pygame.K_q]:
            pygame.quit()
            exit()
        
        pass


    def handleMouseInputs(self, mouse):
        return super().handleMouseInputs(mouse)
    
    def drawDisplay(self, display_surface, TS:TimeSystem):
        test_surface = pygame.Surface((1200,800)).convert_alpha()
        test_surface.fill("light blue")

        time_font = pygame.font.Font(None, 24)
        time_string = "N/A"
        time_display_surface = time_font.render(time_string, False, "Black")
        counter = 0 
        delta_set = 1 

        display_surface.blit(test_surface, (0,0))


        test_health_string = "HEALTH STAT UPDATED ON THE HOUR: " + str(Universe.TEST_HEALTH_STAT)
        ths_display_surface = time_font.render(test_health_string, False, "Black")
        display_surface.blit(ths_display_surface, (250, 250))



        instants_string = str(TS.counter)
        time_display_surface = time_font.render(instants_string, False, "Black")
        display_surface.blit(time_display_surface, (1000, 15))

        hours_string = str(TS.getHours())
        hours_display_surface = time_font.render(hours_string, False, "Blue")
        display_surface.blit(hours_display_surface, (1000, 30))
        days_string = str(TS.getDays())
        days_display_surface = time_font.render(days_string, False, "Blue")
        display_surface.blit(days_display_surface, (1000, 45))
        months_string = str(TS.getMonths())
        months_display_surface = time_font.render(months_string, False, "Red")
        display_surface.blit(months_display_surface, (1000, 60))


        years_string = str(TS.getYears())
        years_display_surface = time_font.render(years_string, False, "Green")
        display_surface.blit(years_display_surface, (1000, 75))

        pass
    
    def handleMusic(self):
        #print("MUSIC STARTED START: " + str(self.music_started))
        
        if self.music_started == False:
            if MusicSystem.jukebox_mode == True:
                return
            else: 
                MusicSystem.play_observing()
                self.music_started = True  # still need to handle coming BACK from another state  
        else:
            pass
       # print("MUSIC STARTED END: " + str(self.music_started))

    def getInternalState(self):
        return super().getInternalState()
    

    def Reset(self): 
        self.internal_state = GamestateIs.OBSERVING
        self.transition_state = GamestateIs.OBSERVING