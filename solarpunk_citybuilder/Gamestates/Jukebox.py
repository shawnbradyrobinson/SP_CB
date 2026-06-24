from Gamestates.Gamestate import Gamestate
from Gamestates.GamestateIs import GamestateIs
from TimeSystem import TimeSystem 

import MusicSystem 
import pygame 

class Jukebox(Gamestate):
    def __init__(self):
        super().__init__()
        self.internal_state = GamestateIs.JUKEBOX
        self.transition_state = GamestateIs.JUKEBOX
        self.music_started = False
        pass 

    def handleKeyInputs(self, keys):
        if keys[pygame.K_RETURN]:
            if MusicSystem.jukebox_mode == False:
                MusicSystem.jukebox_mode = True
            else:
                MusicSystem.jukebox_mode = False
            pass

        if keys[pygame.K_LEFT]:
            MusicSystem.loadAndPlayForever(MusicSystem.SOUNDTRACK[MusicSystem.getPreviousTrackPos()], MusicSystem.getPreviousTrackPos())

        if keys[pygame.K_RIGHT]:
            MusicSystem.loadAndPlayForever(MusicSystem.SOUNDTRACK[MusicSystem.getNextTrackPos()], MusicSystem.getNextTrackPos())

        if keys[pygame.K_j]:
            self.transition_state = GamestateIs.OBSERVING
            print(str(self.transition_state))

        if keys[pygame.K_q]:
            pygame.quit()
            exit()

        pass 
 


    def handleMouseInputs(self, mouse):
        return super().handleMouseInputs(mouse)
    
    def drawDisplay(self, display_surface):
        jukebox_canvas = pygame.Surface((1200, 800)).convert_alpha()
        jukebox_canvas.fill("red")

        jukebox_font = pygame.font.Font(None, 24)

        jukebox_string = "press ENTER to turn jukebox mode on/off \nLEFT ARROW & RIGHT ARROW to switch tracks"
        jbs_surface = jukebox_font.render(jukebox_string, False, "White")
        display_surface.blit(jukebox_canvas, (0, 0))
        display_surface.blit(jbs_surface, (600, 250))



        jukebox_mode_status = " "

        if MusicSystem.jukebox_mode == True:
            jukebox_mode_status = "JUKEBOX: ON"
        else:
            jukebox_mode_status = "JUKEBOX: OFF"
        

        jms_surface = jukebox_font.render(jukebox_mode_status, False, "White")
        display_surface.blit(jms_surface, (0,0))


        previous_track_string = MusicSystem.getPreviousTrack()
        pts_surface = jukebox_font.render(previous_track_string, False, "White")
        
        current_track_string = MusicSystem.getCurrentTrack()
        cts_surface = jukebox_font.render(current_track_string, False, "White")

        next_track_string = MusicSystem.getNextTrack()
        nts_surface = jukebox_font.render(next_track_string, False, "White")

        previous_icon = "<<"
        pi_surface = jukebox_font.render(previous_icon, False, "White")
        


        next_icon = ">>"
        ni_surface = jukebox_font.render(next_icon, False, "White")

        display_surface.blit(pts_surface, (50, 500))
        display_surface.blit(cts_surface, (350, 500))
        display_surface.blit(nts_surface, (950, 500))
        display_surface.blit(pi_surface, (50, 700))
        display_surface.blit(ni_surface, (950, 700))

    
    def getInternalState(self):
        return super().getInternalState()
    
    def Reset(self):
        self.internal_state = GamestateIs.JUKEBOX
        self.transition_state = GamestateIs.JUKEBOX




