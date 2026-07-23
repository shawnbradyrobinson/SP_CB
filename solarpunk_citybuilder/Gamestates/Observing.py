from Gamestates.Gamestate import Gamestate
from Gamestates.GamestateIs import GamestateIs
from TimeSystem import TimeSystem
import MusicSystem
import Universe 
import pygame
import math 

class Observing(Gamestate):
    def __init__(self, gameboard):
        super().__init__()
        self.internal_state = GamestateIs.OBSERVING
        self.transition_state = GamestateIs.OBSERVING
        self.music_started = False 
        self.grid_on = False 
        self.test_surface = pygame.Surface((1200,800)).convert_alpha()
        
        
        #SHORT LOG CAN HOLD 6 
        #LONG LOG CAN HOLD 26
 
        self.log_showing = 1
        self.l_toggle = False
        
        
        
        self.u_toggle = False 
        self.ui_on = True
        self.gameboard = gameboard
        self.CAMERA_SCROLL_RATE = 50 

        self.highlighted = [0, 0]
        self.target_start = [0, 0]
        self.target_end = [0, 0]

        self.quick_status_override = False 
        self.special_status_message = "SPECIAL!"

        self.highlight_fill_color = "pink"

        self.targeting_started = False 

        self.targeted_person = None 


        ## camera[0] x start camera[1] x end camera[2] y start camera[3] y end 
        self.camera = [1200,2400, 800, 1600]
        pass

    def handleKeyInputs(self, keys, TS: TimeSystem):
       
       ## ========= TIME CONTROLS =============== ##
       
        if keys[pygame.K_c]:
            TS.changeDelta(TS.delta * 2)
                
        if keys[pygame.K_z]:
            TS.changeDelta(TS.delta * .5)

        if keys[pygame.K_x]:
            if TS.delta == 0:
                TS.changeDelta(1)
            else: 
                TS.changeDelta(0)
        
        ## ======================================= ## 


        ## ======== CAMERA CONTROLS ============== ## 

        if keys[pygame.K_w]:
            if self.camera[2] == 0:
                return
            else:
                self.camera[2] = self.camera[2] - self.CAMERA_SCROLL_RATE
                self.camera[3] = self.camera[3] - self.CAMERA_SCROLL_RATE

        if keys[pygame.K_a]:
            if self.camera[0] == 0:
                return 
            else:
                self.camera[0] = self.camera[0] - self.CAMERA_SCROLL_RATE
                self.camera[1] = self.camera[1] - self.CAMERA_SCROLL_RATE 

        if keys[pygame.K_s]:
            if self.camera[3] >= self.gameboard.BOARD_SIZE:
                return
            else:
                self.camera[3] = self.camera[3] + self.CAMERA_SCROLL_RATE
                self.camera[2] = self.camera[2] + self.CAMERA_SCROLL_RATE

        if keys[pygame.K_d]:
            if self.camera[1] >= self.gameboard.BOARD_SIZE:
                return
            else:
                self.camera[1] = self.camera[1] + self.CAMERA_SCROLL_RATE
                self.camera[0] = self.camera[0] + self.CAMERA_SCROLL_RATE

        if keys[pygame.K_UP]:
            if self.highlighted[1] == 0:
                self.highlighted[1] = 0
                return 
            else: 
                self.highlighted[1] -= 50 
                return 
            
        if keys[pygame.K_DOWN]:
            if self.highlighted[1] == 800:
                self.highlighted[1] = 800
                return 
            else:
                self.highlighted[1] += 50
                return  

        if keys[pygame.K_RIGHT]:
            if self.highlighted[0] == 1200:
                self.highlighted[0] = 1200 
                return 
            else:
                self.highlighted[0] += 50 
                return 

        if keys[pygame.K_LEFT]:
            if self.highlighted[0] == 0:
                self.highlighted[0] = 0
                return 
            else:
                self.highlighted[0] -= 50 
                return 
        


        if keys[pygame.K_j]:
            self.music_started = False 
            self.transition_state = GamestateIs.JUKEBOX

        if keys[pygame.K_ESCAPE]:
            self.transition_state = GamestateIs.SETTINGS

        if keys[pygame.K_g]:
            if self.grid_on == False:
                self.grid_on = True
                print(self.grid_on) 
            return 
        
        if keys[pygame.K_h]:
            if self.grid_on == True:
                self.grid_on = False
                print(self.grid_on)
            return 
        

        
        if keys[pygame.K_b]:
            self.transition_state = GamestateIs.PLACING


        if keys[pygame.K_u]:
            if not self.u_toggle:
                self.ui_on = not self.ui_on
                self.u_toggle = True 
            else:
                self.u_toggle = False

        if keys[pygame.K_l]:
            if not self.l_toggle:
                if self.log_showing == 0:
                    self.log_showing = 1
                elif self.log_showing == 1:
                    self.log_showing = 2
                elif self.log_showing == 2:
                    self.log_showing = 0 

                self.l_toggle = True
        
        else:
            self.l_toggle = False 


        if keys[pygame.K_m]:
            pygame.mixer.music.stop()

        if keys[pygame.K_q]:
            pygame.quit()
            exit()

        if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]:
            self.highlight_fill_color = "pink"
            self.targeting_started = False 
            self.target_start[0] = 0 
            self.target_start[1] = 0 
            self.quick_status_override = False 
            pass


        if keys[pygame.K_RETURN]:

            absolute_x = math.floor((self.camera[0] + self.highlighted[0]) / 50) 
            absolute_y = math.floor((self.camera[2] + self.highlighted[1]) / 50)
            # absolute_x = math.floor((self.camera[0]) / 50) 
            # absolute_y = math.floor((self.camera[1]) / 50)
            if absolute_x >= 100:
                absolute_x = 100

            if absolute_y >= 100:
                absolute_y = 100


            #GUIDED WALK 
            if self.targeting_started == False: 
                if self.gameboard.board[absolute_x][absolute_y].stood_on == True:
                    self.quick_status_override = True 
                    self.targeted_person = self.gameboard.board[absolute_x][absolute_y].stood_on_by 
                    self.special_status_message = "where should " +self.gameboard.board[absolute_x][absolute_y].stood_on_by.first_name +" go?\nshift to cancel"
                
                    self.target_start[0] = absolute_x 
                    self.target_start[1] = absolute_y

                    self.targeting_started = True 

                    self.highlight_fill_color = "yellow"
                else: 
                    pass           
            else:
                self.target_end[0] = absolute_x
                self.target_end[1] = absolute_y
                
                if self.gameboard.board[absolute_x][absolute_y].tileWalkable() == True:
                    self.highlight_fill_color = "pink"
                    self.quick_status_override = False

                    self.targeted_person.start_guided_walk(self.target_end)


                    pass
                else:
                    self.special_status_message = "can't walk there, silly!\nshift to cancel"  
                    return 



                self.quick_status_override = False
                self.targeting_started = False  
                self.targeted_person = None 
                pass 

        
        if keys[pygame.K_p]:
            self.transition_state = GamestateIs.PEOPLE
            return 
        
        pass


    def handleMouseInputs(self, mouse):
        return super().handleMouseInputs(mouse)
    
    def drawDisplay(self, display_surface, TS:TimeSystem):
        self.test_surface
        self.test_surface.fill("aliceblue")

        observing_font = pygame.font.Font(None, 22)

        display_surface.blit(self.test_surface, (0,0))


        test_health_string = "HEALTH STAT UPDATED ON THE HOUR: " + str(Universe.TEST_HEALTH_STAT)
        ths_display_surface = observing_font.render(test_health_string, False, "Black")
        display_surface.blit(ths_display_surface, (250, 250))



        # ============== ADVENTURE LOG UI ============================================ # 
        short_adventure_log_surface = pygame.Surface((400, 100)).convert_alpha()
        short_adventure_log_surface.fill("grey20")
        adventure_log_font = pygame.font.Font(None, 20)
        assembled_logs = " "

        if self.log_showing == 1: 
            i = 5
            while i >= 0: 
               assembled_logs += Universe.adventure_logs[(len(Universe.adventure_logs)-1)- i] + "\n"
               i -= 1 
        elif self.log_showing == 2: 
            for i in range(len(Universe.adventure_logs)):
                assembled_logs += Universe.adventure_logs[i] + "\n"
                pass 

        
        lt_surface = adventure_log_font.render(assembled_logs, False, "greenyellow")
        short_adventure_log_surface.blit(lt_surface, (5, 5))


        long_adventure_log_surface = pygame.Surface((400, 400)).convert_alpha()
        long_adventure_log_surface.fill("grey20")
        long_adventure_log_surface.blit(lt_surface, (5,5))



        # ============== END OF ADVENTURE LOG UI ==================================== # 




        # ========== QUICK STATUS UI =============================== #
        quick_status_surface = pygame.Surface((400, 50)).convert_alpha()
        quick_status_surface.fill("antiquewhite3")
        quick_status_font = pygame.font.Font(None, 26)
        if self.quick_status_override == False:
            quick_status_string = self.getQuickStatus(self.highlighted[0], self.highlighted[1])
        else: 
            quick_status_string = self.special_status_message  
        
        qss_surface = quick_status_font.render(quick_status_string, False, "Black")
        quick_status_surface.blit(qss_surface, (100,15))





        # ========== END QUICK STATUS UI ============================ #


        # ============ CITY STATS DISPLAY UI ========================= #

        city_stats_surface = pygame.Surface((200, 100)).convert_alpha()
        city_stats_surface.fill("antiquewhite1")
        population_string = "POPULATION: " +str(Universe.getTotalPersonAmount())
        pop_surface = observing_font.render(population_string, False, "Black")
        #population_icon = pygame.image.load("graphics/population_icon_test.png").convert_alpha()


        food_status_string = "FOOD:     " +Universe.getFoodStatusString()
        fs_surface = observing_font.render(food_status_string, False, "Black")

        peace_string = "PEACE:            " +str(Universe.getPeaceLevel())
        ps_surface = observing_font.render(peace_string, False, "Black")

        community_level_string = "COMM. LVL:     " +str(Universe.getCommunityLevel())
        cl_surface = observing_font.render(community_level_string, False, "Black")
        #city_stats_surface.blit(population_icon, (0, 15))
        city_stats_surface.blit(pop_surface, (0, 0))
        city_stats_surface.blit(fs_surface, (0, 20))
        city_stats_surface.blit(ps_surface, (0, 40))
        city_stats_surface.blit(cl_surface, (0, 60))
        

        # =========== END CITY STATS DISPLAY UI ======================= #


        #dummy_dude = pygame.image.load("graphics/dummy_dude.png").convert_alpha()


        # =============== TIME DISPLAY UI ===================================== # 
        time_font = pygame.font.Font(None, 22)
        time_string = "N/A"
        time_string_surface = time_font.render(time_string, False, "Black")
        counter = 0 
        delta_set = 1 
        time_display_surface = pygame.Surface((200, 100)).convert_alpha()
        time_display_surface.fill("gray90")



        # instants_string = str(TS.counter)
        instants_string = "[z]slow fast[c]\n-------------"
        instants_bar_surface = pygame.Surface((100, 5)).convert_alpha()
        instants_bar_surface.fill("cornflowerblue")
        for i in range(int(TS.counter / 10)):
            time_display_surface.blit(instants_bar_surface, (100, i))
        instants_display_surface = time_font.render(instants_string, False, "Black")
        time_display_surface.blit(instants_display_surface, (0, 0))

        hours_string = "HOUR:        " + str(TS.getHours())
        hours_display_surface = time_font.render(hours_string, False, "Black")
        time_display_surface.blit(hours_display_surface, (0, 30))
        
        days_string = "DAY:            " + str(TS.getDays())
        days_display_surface = time_font.render(days_string, False, "Black")
        time_display_surface.blit(days_display_surface, (0, 45))
        
        months_string = "MONTH:    " + str(TS.getMonths())
        months_display_surface = time_font.render(months_string, False, "Black")
        time_display_surface.blit(months_display_surface, (0, 60))


        years_string = "YEAR:    " + str(TS.getYears())
        years_display_surface = time_font.render(years_string, False, "Black")
        time_display_surface.blit(years_display_surface, (0, 75))

        # =============== END OF TIME DISPLAY UI ===================================== # 
        
        
        
        # =============== BOTTOM BAR UI =============================================== #
        bottom_bar_surface = pygame.Surface((1000, 75)).convert_alpha()
        bottom_bar_surface.fill("brown")
        bar_font = pygame.font.Font(None, 28)

        people_command_box = pygame.Surface((200, 75)).convert_alpha()
        people_command_box.fill("brown1")
        people_command_string = "PEOPLE\n[P]"
        pcs_surface = bar_font.render(people_command_string, False, "White")
        people_command_box.blit(pcs_surface, (50, 10))


        build_command_box = pygame.Surface((200, 75)).convert_alpha()
        build_command_box.fill("brown2")
        build_command_string  = "BUILD\n[B]"
        bcs_surface = bar_font.render(build_command_string, False, "White")
        build_command_box.blit(bcs_surface, (50, 10))



        status_command_box = pygame.Surface((200, 75)).convert_alpha()
        status_command_box.fill("brown3")
        status_command_string = "INFO\n[I]"
        scs_surface = bar_font.render(status_command_string, False, "White")
        status_command_box.blit(scs_surface, (50, 10))


        govern_command_box = pygame.Surface((200, 75)).convert_alpha()
        govern_command_box.fill("brown4")
        govern_command_string = "GOVERN\n[G]"
        gcs_surface = bar_font.render(govern_command_string, False, "White")
        govern_command_box.blit(gcs_surface, (50, 10))

        menu_adventure_box = pygame.Surface((200, 75)).convert_alpha()
        menu_adventure_box.fill("brown")
        menu_adventure_string = "MENU - LOG\n[ESC] -  [L]"
        mas_surface = bar_font.render(menu_adventure_string, False, "White")
        menu_adventure_box.blit(mas_surface, (50, 10))

        bottom_bar_surface.blit(people_command_box, (0, 0))
        bottom_bar_surface.blit(build_command_box, (200, 0))
        bottom_bar_surface.blit(status_command_box, (400, 0))
        bottom_bar_surface.blit(govern_command_box, (600, 0))
        bottom_bar_surface.blit(menu_adventure_box, (800, 0))


        # ============== END OF BOTTOM BAR UI ========================================== #         
        
        
        current_game_board = self.gameboard.drawCurrentBoard(self.camera[0], self.camera[1], self.camera[2], self.camera[3])

        display_surface.blit(current_game_board, (0,0))


        ## =========== DRAW HIGHLIGHT =============== ## 
        highlight_px = pygame.Surface((3,3)).convert_alpha()
        highlight_px.fill(self.highlight_fill_color)
        
        for i in range (0, 50):
            display_surface.blit(highlight_px, (self.highlighted[0]+i, self.highlighted[1]))
        
        for j in range (0, 50):
            display_surface.blit(highlight_px, (self.highlighted[0], self.highlighted[1]+j))

        for k in range (0, 50):
            display_surface.blit(highlight_px, (self.highlighted[0]+50, self.highlighted[1]+k))

        for l in range (0, 50):
            display_surface.blit(highlight_px, (self.highlighted[0]+l, self.highlighted[1]+50))

        ## =========================================== ## 

        # ============= PUTTING IT ALL TOGETHER =================================
        if self.ui_on == True:
            if self.log_showing == 1:
                display_surface.blit(short_adventure_log_surface, (0,0))
            elif self.log_showing == 2:
                display_surface.blit(long_adventure_log_surface, (0,0))
            else:
                pass
            display_surface.blit(time_display_surface, (1000, 0))
            display_surface.blit(quick_status_surface, (400, 0))
            display_surface.blit(city_stats_surface, (800, 0))
            display_surface.blit(bottom_bar_surface, (100, 715))
            #display_surface.blit(dummy_dude, (600, 400))
            # draw_test = pygame.Surface((50, 50)).convert_alpha()
            # draw_test.fill("black")
            # display_surface.blit(draw_test, (600, 400))
        else: 
            pass 
        # =============== :-) ================================================
        
        
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

    def drawGrid(self, display_surface):
        list = [0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200]
        for i in list:
            pygame.draw.line(display_surface, "Black", (0, 1*i), (1200, 1*i), 1)

        for j in list:
            pygame.draw.line(display_surface, "Black", (1*j, 0),(1*j, 800), 1)

    def getQuickStatus(self, h_x, h_y) -> str:
        absolute_x = math.floor((self.camera[0] + h_x) / 50) 
        absolute_y = math.floor((self.camera[2] + h_y) / 50)
        # absolute_x = math.floor((self.camera[0]) / 50) 
        # absolute_y = math.floor((self.camera[1]) / 50)
        if absolute_x >= 100:
            absolute_x = 100

        if absolute_y >= 100:
            absolute_y = 100
        
        #print("ABS X " +str(absolute_x) + " HIGH X " + str(h_x) + " CAM[0] " + str(self.camera[0]))
        #print("ABS Y " +str(absolute_y)+ " HIGH Y " + str(h_y) + " CAM[2] " + str(self.camera[2])) 

        return str(self.gameboard.board[absolute_x][absolute_y].external)


