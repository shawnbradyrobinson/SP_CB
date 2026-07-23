from Gamestates.Gamestate import Gamestate
from Gamestates.GamestateIs import GamestateIs
from TimeSystem import TimeSystem
import MusicSystem
import Universe
import pygame
import math 
import itertools


class People(Gamestate):
    def __init__(self):
        super().__init__()
        self.people_canvas = pygame.Surface((1200, 800)).convert_alpha()
        self.internal_state = GamestateIs.PEOPLE
        self.transition_state = GamestateIs.PEOPLE
        self.page_positions = [None, None, None, None, None, None, None, None]
        self.page_num = 1
        self.createPeoplePages(self.page_num)
        pass 


    def handleKeyInputs(self, keys):
        if keys[pygame.K_p]:
            self.transition_state = GamestateIs.OBSERVING
            return 
        if keys[pygame.K_ESCAPE]:
            self.transition_state = GamestateIs.SETTINGS
            return 
        
        if keys[pygame.K_LEFT]:
            if self.page_num == 1:
                self.page_num = 1
            else:
                self.page_num -= 1

            self.createPeoplePages(self.page_num)
        
        if keys[pygame.K_RIGHT]:
            if (self.page_num*8) > len(Universe.persons_dict):
                return 
            else:
                self.page_num += 1 
            self.createPeoplePages(self.page_num)

    def handleMouseInputs(self, mouse):
        return super().handleMouseInputs(mouse)
    

    def drawDisplay(self, display_surface):
        self.people_canvas
        self.people_canvas.fill("lavender")

        people_standard_font = pygame.font.Font(None, 28)
        people_title_font = pygame.font.Font(None, 72)

        display_surface.blit(self.people_canvas, (0, 0))

        # =========== SCREEN TITLE ================= #
        screen_title_surface = pygame.Surface((1200, 100)).convert_alpha()
        screen_title_surface.fill("lavender")
        people_screen_title_string = "COMMUNITY REGISTRY"
        psts_surface = people_title_font.render(people_screen_title_string, False, "Black")
        
        screen_title_surface.blit(psts_surface, (500, 10))

        people_controls_instructions_string = "Use WASD to navigate, LEFT / RIGHT to flip pages"
        pcis_surface = people_standard_font.render(people_controls_instructions_string, False, "Black")
        screen_title_surface.blit(pcis_surface, (375, 75))
        # ============================================= # 


        # =========== PERSONS PAGINATION =============== # 

        persons_display_surface = pygame.Surface((1200, 700)).convert_alpha()
        persons_display_surface.fill("lavender")
        BLURB_X = 550
        BLURB_Y = 100 
        BLURB_COLOR = "purple"
        page_number = str(self.page_num)
        page_number_surface = people_title_font.render(page_number, False, "Black")

        people_blurb_one = pygame.Surface((BLURB_X, BLURB_Y))
        people_blurb_one.fill(BLURB_COLOR)
        blurb_one_profile_pic = None 
        blurb_one_info_box = pygame.Surface((500, 100))
        blurb_one_info_box.fill("purple")

        if self.page_positions[0] != None:
            blurb_one_profile_pic = self.page_positions[0].surface_sprite 
           
            person_name = self.page_positions[0].person_name 
            pn = people_standard_font.render(person_name, False, "White")

            person_status = "STATUS: " +self.page_positions[0].person_status 
            ps = people_standard_font.render(person_status, False, "White")

            currently_delegated = "DELEGATED: " +str(self.page_positions[0].currently_delegated)
            cd = people_standard_font.render(currently_delegated, False, "White")
            
            person_age = "AGE: " +str(self.page_positions[0].age) 
            age = people_standard_font.render(person_age, False, "White")

            hunger_level = "HUNGER: " +str(self.page_positions[0].hunger_level)
            hl = people_standard_font.render(hunger_level, False, "White")

            thirst_level = "THIRST: " +str(self.page_positions[0].thirst_level)
            tl = people_standard_font.render(thirst_level, False, "White")

            vigor        = "VIGOR: " +str(self.page_positions[0].vigor) 
            vg = people_standard_font.render(vigor, False, "White")

            overall_proficiency = "OVR PROF: " +str(self.page_positions[0].overall_proficiency)
            op = people_standard_font.render(overall_proficiency, False, "White")

            blurb_one_info_box.blit(pn, (0,0))
            blurb_one_info_box.blit(ps, (0, 30))
            blurb_one_info_box.blit(cd, (0, 50))
            blurb_one_info_box.blit(age, (0, 70))

            blurb_one_info_box.blit(hl, (300, 10))
            blurb_one_info_box.blit(tl, (300, 30))
            blurb_one_info_box.blit(vg, (300, 50))
            blurb_one_info_box.blit(op, (300, 70))
        else:
            blurb_one_profile_pic = pygame.Surface((50, 50))
            blurb_one_profile_pic.fill("gray")
            blurb_one_info_box.fill("grey20")
        
        people_blurb_one.blit(blurb_one_profile_pic, (0, 0))
        people_blurb_one.blit(blurb_one_info_box, (50, 0))
        #
        people_blurb_two = pygame.Surface((BLURB_X, BLURB_Y))
        people_blurb_two.fill(BLURB_COLOR)
        blurb_two_profile_pic = None
        blurb_two_info_box = pygame.Surface((500, 100))
        blurb_two_info_box.fill("purple")

        if self.page_positions[1] != None:
            blurb_two_profile_pic = self.page_positions[1].surface_sprite

            person_name = self.page_positions[1].person_name 
            pn = people_standard_font.render(person_name, False, "White")

            person_status = "STATUS: " +self.page_positions[1].person_status 
            ps = people_standard_font.render(person_status, False, "White")

            currently_delegated = "DELEGATED: " +str(self.page_positions[1].currently_delegated)
            cd = people_standard_font.render(currently_delegated, False, "White")
            
            person_age = "AGE: " +str(self.page_positions[1].age) 
            age = people_standard_font.render(person_age, False, "White")

            hunger_level = "HUNGER: " +str(self.page_positions[1].hunger_level)
            hl = people_standard_font.render(hunger_level, False, "White")

            thirst_level = "THIRST: " +str(self.page_positions[1].thirst_level)
            tl = people_standard_font.render(thirst_level, False, "White")

            vigor        = "VIGOR: " +str(self.page_positions[1].vigor) 
            vg = people_standard_font.render(vigor, False, "White")

            overall_proficiency = "OVR PROF: " +str(self.page_positions[1].overall_proficiency)
            op = people_standard_font.render(overall_proficiency, False, "White")

            blurb_two_info_box.blit(pn, (0,0))
            blurb_two_info_box.blit(ps, (0, 30))
            blurb_two_info_box.blit(cd, (0, 50))
            blurb_two_info_box.blit(age, (0, 70))

            blurb_two_info_box.blit(hl, (300, 10))
            blurb_two_info_box.blit(tl, (300, 30))
            blurb_two_info_box.blit(vg, (300, 50))
            blurb_two_info_box.blit(op, (300, 70))
        else:
            blurb_two_profile_pic = pygame.Surface((50, 50))
            blurb_two_profile_pic.fill("gray")
        people_blurb_two.blit(blurb_two_profile_pic, (0, 0))
        people_blurb_two.blit(blurb_two_info_box, (50, 0))

        people_blurb_three = pygame.Surface((BLURB_X, BLURB_Y))
        people_blurb_three.fill(BLURB_COLOR)
        blurb_three_profile_pic = None
        blurb_three_info_box = pygame.Surface((500, 100))
        blurb_three_info_box.fill("purple")
        if self.page_positions[2] != None:
            blurb_three_profile_pic = self.page_positions[2].surface_sprite 

            person_name = self.page_positions[2].person_name 
            pn = people_standard_font.render(person_name, False, "White")

            person_status = "STATUS: " +self.page_positions[2].person_status 
            ps = people_standard_font.render(person_status, False, "White")

            currently_delegated = "DELEGATED: " +str(self.page_positions[2].currently_delegated)
            cd = people_standard_font.render(currently_delegated, False, "White")
            
            person_age = "AGE: " +str(self.page_positions[2].age) 
            age = people_standard_font.render(person_age, False, "White")

            hunger_level = "HUNGER: " +str(self.page_positions[2].hunger_level)
            hl = people_standard_font.render(hunger_level, False, "White")

            thirst_level = "THIRST: " +str(self.page_positions[2].thirst_level)
            tl = people_standard_font.render(thirst_level, False, "White")

            vigor        = "VIGOR: " +str(self.page_positions[2].vigor) 
            vg = people_standard_font.render(vigor, False, "White")

            overall_proficiency = "OVR PROF: " +str(self.page_positions[2].overall_proficiency)
            op = people_standard_font.render(overall_proficiency, False, "White")

            blurb_three_info_box.blit(pn, (0,0))
            blurb_three_info_box.blit(ps, (0, 30))
            blurb_three_info_box.blit(cd, (0, 50))
            blurb_three_info_box.blit(age, (0, 70))

            blurb_three_info_box.blit(hl, (300, 10))
            blurb_three_info_box.blit(tl, (300, 30))
            blurb_three_info_box.blit(vg, (300, 50))
            blurb_three_info_box.blit(op, (300, 70))
        else:
            blurb_three_profile_pic = pygame.Surface((50, 50))
            blurb_three_profile_pic.fill("gray")
        people_blurb_three.blit(blurb_three_profile_pic, (0,0))
        people_blurb_three.blit(blurb_three_info_box, (50, 0))

        people_blurb_four = pygame.Surface((BLURB_X, BLURB_Y))
        people_blurb_four.fill(BLURB_COLOR)
        blurb_four_profile_pic = None
        blurb_four_info_box = pygame.Surface((500, 100))
        blurb_four_info_box.fill("purple")
        if self.page_positions[3] != None:
            blurb_four_profile_pic = self.page_positions[3].surface_sprite

            person_name = self.page_positions[3].person_name 
            pn = people_standard_font.render(person_name, False, "White")

            person_status = "STATUS: " +self.page_positions[3].person_status 
            ps = people_standard_font.render(person_status, False, "White")

            currently_delegated = "DELEGATED: " +str(self.page_positions[3].currently_delegated)
            cd = people_standard_font.render(currently_delegated, False, "White")
            
            person_age = "AGE: " +str(self.page_positions[3].age) 
            age = people_standard_font.render(person_age, False, "White")

            hunger_level = "HUNGER: " +str(self.page_positions[3].hunger_level)
            hl = people_standard_font.render(hunger_level, False, "White")

            thirst_level = "THIRST: " +str(self.page_positions[3].thirst_level)
            tl = people_standard_font.render(thirst_level, False, "White")

            vigor        = "VIGOR: " +str(self.page_positions[3].vigor) 
            vg = people_standard_font.render(vigor, False, "White")

            overall_proficiency = "OVR PROF: " +str(self.page_positions[3].overall_proficiency)
            op = people_standard_font.render(overall_proficiency, False, "White")

            blurb_four_info_box.blit(pn, (0,0))
            blurb_four_info_box.blit(ps, (0, 30))
            blurb_four_info_box.blit(cd, (0, 50))
            blurb_four_info_box.blit(age, (0, 70))

            blurb_four_info_box.blit(hl, (300, 10))
            blurb_four_info_box.blit(tl, (300, 30))
            blurb_four_info_box.blit(vg, (300, 50))
            blurb_four_info_box.blit(op, (300, 70))
        else:
            blurb_four_profile_pic = pygame.Surface((50, 50))
            blurb_four_profile_pic.fill("gray")
        people_blurb_four.blit(blurb_four_profile_pic, (0,0))
        people_blurb_four.blit(blurb_four_info_box, (50, 0))

        people_blurb_five = pygame.Surface((BLURB_X, BLURB_Y))
        people_blurb_five.fill(BLURB_COLOR)
        blurb_five_profile_pic = None
        blurb_five_info_box = pygame.Surface((500, 100))
        blurb_five_info_box.fill("purple")

        if self.page_positions[4] != None:
            blurb_five_profile_pic = self.page_positions[4].surface_sprite

            person_name = self.page_positions[4].person_name 
            pn = people_standard_font.render(person_name, False, "White")

            person_status = "STATUS: " +self.page_positions[4].person_status 
            ps = people_standard_font.render(person_status, False, "White")

            currently_delegated = "DELEGATED: " +str(self.page_positions[4].currently_delegated)
            cd = people_standard_font.render(currently_delegated, False, "White")
            
            person_age = "AGE: " +str(self.page_positions[4].age) 
            age = people_standard_font.render(person_age, False, "White")

            hunger_level = "HUNGER: " +str(self.page_positions[4].hunger_level)
            hl = people_standard_font.render(hunger_level, False, "White")

            thirst_level = "THIRST: " +str(self.page_positions[4].thirst_level)
            tl = people_standard_font.render(thirst_level, False, "White")

            vigor        = "VIGOR: " +str(self.page_positions[4].vigor) 
            vg = people_standard_font.render(vigor, False, "White")

            overall_proficiency = "OVR PROF: " +str(self.page_positions[4].overall_proficiency)
            op = people_standard_font.render(overall_proficiency, False, "White")

            blurb_five_info_box.blit(pn, (0,0))
            blurb_five_info_box.blit(ps, (0, 30))
            blurb_five_info_box.blit(cd, (0, 50))
            blurb_five_info_box.blit(age, (0, 70))

            blurb_five_info_box.blit(hl, (300, 10))
            blurb_five_info_box.blit(tl, (300, 30))
            blurb_five_info_box.blit(vg, (300, 50))
            blurb_five_info_box.blit(op, (300, 70))
        else:
            blurb_five_profile_pic = pygame.Surface((50, 50))
            blurb_five_profile_pic.fill("gray")
        people_blurb_five.blit(blurb_five_profile_pic, (0,0))
        people_blurb_five.blit(blurb_five_info_box, (50, 0))


        people_blurb_six = pygame.Surface((BLURB_X, BLURB_Y))
        people_blurb_six.fill(BLURB_COLOR)
        blurb_six_profile_pic = None
        blurb_six_info_box = pygame.Surface((500, 100))
        blurb_six_info_box.fill("purple")
        if self.page_positions[5] != None:
            blurb_six_profile_pic = self.page_positions[5].surface_sprite 

            person_name = self.page_positions[5].person_name 
            pn = people_standard_font.render(person_name, False, "White")

            person_status = "STATUS: " +self.page_positions[5].person_status 
            ps = people_standard_font.render(person_status, False, "White")

            currently_delegated = "DELEGATED: " +str(self.page_positions[5].currently_delegated)
            cd = people_standard_font.render(currently_delegated, False, "White")
            
            person_age = "AGE: " +str(self.page_positions[5].age) 
            age = people_standard_font.render(person_age, False, "White")

            hunger_level = "HUNGER: " +str(self.page_positions[5].hunger_level)
            hl = people_standard_font.render(hunger_level, False, "White")

            thirst_level = "THIRST: " +str(self.page_positions[5].thirst_level)
            tl = people_standard_font.render(thirst_level, False, "White")

            vigor        = "VIGOR: " +str(self.page_positions[5].vigor) 
            vg = people_standard_font.render(vigor, False, "White")

            overall_proficiency = "OVR PROF: " +str(self.page_positions[5].overall_proficiency)
            op = people_standard_font.render(overall_proficiency, False, "White")

            blurb_six_info_box.blit(pn, (0,0))
            blurb_six_info_box.blit(ps, (0, 30))
            blurb_six_info_box.blit(cd, (0, 50))
            blurb_six_info_box.blit(age, (0, 70))

            blurb_six_info_box.blit(hl, (300, 10))
            blurb_six_info_box.blit(tl, (300, 30))
            blurb_six_info_box.blit(vg, (300, 50))
            blurb_six_info_box.blit(op, (300, 70))
        else:
            blurb_six_profile_pic = pygame.Surface((50, 50))
            blurb_six_profile_pic.fill("gray") 
        people_blurb_six.blit(blurb_six_profile_pic, (0,0))
        people_blurb_six.blit(blurb_six_info_box, (50, 0))


        people_blurb_seven = pygame.Surface((BLURB_X, BLURB_Y))
        people_blurb_seven.fill(BLURB_COLOR)
        blurb_seven_profile_pic = None
        blurb_seven_info_box = pygame.Surface((500, 100))
        blurb_seven_info_box.fill("purple")
        if self.page_positions[6] != None:
            blurb_seven_profile_pic = self.page_positions[6].surface_sprite

            person_name = self.page_positions[6].person_name 
            pn = people_standard_font.render(person_name, False, "White")

            person_status = "STATUS: " +self.page_positions[6].person_status 
            ps = people_standard_font.render(person_status, False, "White")

            currently_delegated = "DELEGATED: " +str(self.page_positions[6].currently_delegated)
            cd = people_standard_font.render(currently_delegated, False, "White")
            
            person_age = "AGE: " +str(self.page_positions[6].age) 
            age = people_standard_font.render(person_age, False, "White")

            hunger_level = "HUNGER: " +str(self.page_positions[6].hunger_level)
            hl = people_standard_font.render(hunger_level, False, "White")

            thirst_level = "THIRST: " +str(self.page_positions[6].thirst_level)
            tl = people_standard_font.render(thirst_level, False, "White")

            vigor        = "VIGOR: " +str(self.page_positions[6].vigor) 
            vg = people_standard_font.render(vigor, False, "White")

            overall_proficiency = "OVR PROF: " +str(self.page_positions[6].overall_proficiency)
            op = people_standard_font.render(overall_proficiency, False, "White")

            blurb_seven_info_box.blit(pn, (0,0))
            blurb_seven_info_box.blit(ps, (0, 30))
            blurb_seven_info_box.blit(cd, (0, 50))
            blurb_seven_info_box.blit(age, (0, 70))

            blurb_seven_info_box.blit(hl, (300, 10))
            blurb_seven_info_box.blit(tl, (300, 30))
            blurb_seven_info_box.blit(vg, (300, 50))
            blurb_seven_info_box.blit(op, (300, 70))
        else:
            blurb_seven_profile_pic = pygame.Surface((50, 50))
            blurb_seven_profile_pic.fill("gray") 
        people_blurb_seven.blit(blurb_seven_profile_pic, (0,0))
        people_blurb_seven.blit(blurb_seven_info_box, (50, 0))

        people_blurb_eight = pygame.Surface((BLURB_X, BLURB_Y))
        people_blurb_eight.fill(BLURB_COLOR)
        blurb_eight_profile_pic = None
        blurb_eight_info_box = pygame.Surface((500, 100))
        blurb_eight_info_box.fill("purple")
        if self.page_positions[7] != None:
            blurb_eight_profile_pic = self.page_positions[7].surface_sprite

            person_name = self.page_positions[7].person_name 
            pn = people_standard_font.render(person_name, False, "White")

            person_status = "STATUS: " +self.page_positions[7].person_status 
            ps = people_standard_font.render(person_status, False, "White")

            currently_delegated = "DELEGATED: " +str(self.page_positions[7].currently_delegated)
            cd = people_standard_font.render(currently_delegated, False, "White")
            
            person_age = "AGE: " +str(self.page_positions[7].age) 
            age = people_standard_font.render(person_age, False, "White")

            hunger_level = "HUNGER: " +str(self.page_positions[7].hunger_level)
            hl = people_standard_font.render(hunger_level, False, "White")

            thirst_level = "THIRST: " +str(self.page_positions[7].thirst_level)
            tl = people_standard_font.render(thirst_level, False, "White")

            vigor        = "VIGOR: " +str(self.page_positions[7].vigor) 
            vg = people_standard_font.render(vigor, False, "White")

            overall_proficiency = "OVR PROF: " +str(self.page_positions[7].overall_proficiency)
            op = people_standard_font.render(overall_proficiency, False, "White")

            blurb_eight_info_box.blit(pn, (0,0))
            blurb_eight_info_box.blit(ps, (0, 30))
            blurb_eight_info_box.blit(cd, (0, 50))
            blurb_eight_info_box.blit(age, (0, 70))

            blurb_eight_info_box.blit(hl, (300, 10))
            blurb_eight_info_box.blit(tl, (300, 30))
            blurb_eight_info_box.blit(vg, (300, 50))
            blurb_eight_info_box.blit(op, (300, 70))
        else:
            blurb_eight_profile_pic = pygame.Surface((50,50))
            blurb_eight_profile_pic.fill("gray")
        people_blurb_eight.blit(blurb_eight_profile_pic, (0,0))
        people_blurb_eight.blit(blurb_eight_info_box, (50, 0))

        persons_display_surface.blit(people_blurb_one, (50, 0))
        persons_display_surface.blit(people_blurb_two, (50, 150))
        persons_display_surface.blit(people_blurb_three, (50, 300))
        persons_display_surface.blit(people_blurb_four, (50, 450))
        persons_display_surface.blit(people_blurb_five, (625, 0))
        persons_display_surface.blit(people_blurb_six, (625, 150))
        persons_display_surface.blit(people_blurb_seven, (625, 300))
        persons_display_surface.blit(people_blurb_eight, (625, 450))
        




        # =============================================== # 


        # ============== PUTTING IT ALL TOGETHER ======== #

        display_surface.blit(screen_title_surface, (0, 0))
        display_surface.blit(persons_display_surface, (0, 100))
        display_surface.blit(page_number_surface, (600, 700))
        # =============================================== # 



    def Reset(self):
        self.internal_state = GamestateIs.PEOPLE
        self.transition_state = GamestateIs.PEOPLE

    def getInternalState(self):
        return super().getInternalState()
    
    def createPeoplePages(self, page_num: int):
        person_pages_dict = dict(itertools.islice(Universe.persons_dict.items(), ((page_num-1) *8), 8 * page_num))
        i = 0 
        for person in person_pages_dict.keys():
            print(person)
            peep = person_pages_dict[person] 
            self.page_positions[i] = peep
            i += 1 
        
        
