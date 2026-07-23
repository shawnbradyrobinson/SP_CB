from Entity import Entity 
from Inventory import Inventory
import pygame 
import random 
import Gameboard 
import Universe 

class Person(Entity):
    "Generic starting point for all persons"
    def __init__(self, person_name: str):
        Entity.__init__(self, person_name)
        name_split = person_name.split()
        self.person_name = person_name
        self.first_name = name_split[0]
        self.last_name = name_split[1]
        self.surface_sprite = pygame.image.load("graphics/dummy_dude.png").convert_alpha()

        self.person_pos_x = 0 
        self.person_pos_y = 0 
        
        self.person_status = "is idle"
        self.currently_delegated = False 

        self.headed_toward = [0,0]


        self.age = 20
        #hunger level is 0-10...0 = full, 10= starving
        self.hunger_level = 0

        self.thirst_level = 0 
        #injury state is 0-10... 0=none 10=fully incapacitated by injury
        self.injury_state = 0 
        #illness state is 0-10... 0=healthy 10= deathly ill 
        self.illness_state = 0
        #vigor is how actively they perform in life; vitality, energy...
        # 0 - 100 
        self.vigor = 50

        # the funnel to which all minor proficiencys get converted...how GOOD 
        #are they at doing stuff?? 0 - 100 
        self.overall_proficiency = 50 
        self.personal_inventory = Inventory()

        #self.work_interest
        #self.personal_interest

    def fullInit(self, age: int, hunger_level: int, thirst_level: int, injury_state: int, illness_state: int, vigor: int, overall_proficiency: int, inventory_preset: Inventory.Inventory): 
        self.age = age
        self.hunger_level = hunger_level
        self.thirst_level = thirst_level 
        self.injury_state = injury_state
        self.illness_state = illness_state
        self.vigor = vigor 
        self.overall_proficiency = overall_proficiency
        self.personal_inventory = inventory_preset

    def changeName(self, new_name: str):
        self.person_name = new_name 

    def changeAge(self, new_age: int):
        self.age = new_age
    
    def changeHungerLevel(self, new_level: int):
        self.hunger_level = new_level
    
    def changeInjuryState(self, new_state: int):
        self.injury_state = new_state

    def changeIllnessState(self, new_state: int):
        self.illness_state = new_state

    def changeVigor(self, new_vigor: int):
        self.vigor = new_vigor

    def changeOverallProficiency(self, new_ovr: int): 
        self.overall_proficiency = new_ovr

    def getName(self):
        return self.person_name 

    def getAge(self):
        return self.age
    
    def getHungerLevel(self):
        return self.hunger_level
    
    def getInjuryState(self):
        return self.injury_state

    def getIllnessState(self):
        return self.illness_state

    def getVigor(self):
        return self.vigor

    def getOverallProficiency(self):
        return self.overall_proficiency
    

    def random_walk(self, gameboard: Gameboard):
        #random walking for now 
        walk_choice = int(random.uniform(0,10))

        gameboard.board[self.person_pos_x][self.person_pos_y].stood_on = False 
        gameboard.board[self.person_pos_x][self.person_pos_y].stood_on_by = None 
        
        starting_spot_x = self.person_pos_x
        starting_spot_y = self.person_pos_y 

        #stay in place 
        if walk_choice == 0:
            pass 

        elif walk_choice == 1 or walk_choice == 2:
            if self.person_pos_x + 1 <= 99:
                self.person_pos_x = self.person_pos_x + 1 
            else:
                self.person_pos_x = 99
        elif walk_choice == 3 or walk_choice == 4:
            if self.person_pos_y + 1 <= 99:
                self.person_pos_y = self.person_pos_y + 1
            else:
                self.person_pos_y = 99

        elif walk_choice == 5 or walk_choice == 6:
            if self.person_pos_x - 1 >= 0:
                self.person_pos_x = self.person_pos_x - 1
            else: 
                self.person_pos_x = 0 
        
        elif walk_choice == 7 or walk_choice == 8:
            if self.person_pos_y - 1 >= 0:
                self.person_pos_y = self.person_pos_y - 1 
            else:
                self.person_pos_y = 0 
        else:
            pass 
        
        if gameboard.board[self.person_pos_x][self.person_pos_y].tileWalkable() == True:
            gameboard.board[self.person_pos_x][self.person_pos_y].stood_on = True 
            gameboard.board[self.person_pos_x][self.person_pos_y].stood_on_by = self
        else:
            self.person_pos_x = starting_spot_x
            self.person_pos_y = starting_spot_y
            gameboard.board[self.person_pos_x][self.person_pos_y].stood_on = True 
            gameboard.board[self.person_pos_x][self.person_pos_y].stood_on_by = self 

    def start_guided_walk(self, destination_target: list):
        #Change icon to "on a mission"
        self.currently_delegated = True 
        self.headed_toward[0] = destination_target[0]
        self.headed_toward[1] = destination_target[1]
        self.person_status = "is walking to " +str(self.headed_toward[0]) +" , " + str(self.headed_toward[1])

    def continue_guided_walk(self, gameboard: Gameboard):
        if self.hasReachedDestination() == True:
            self.currently_delegated = False
            self.headed_toward[0] = 0 
            self.headed_toward[1] = 0 
            Universe.addAdventureLog(self.first_name + " reached their destination!")
            self.person_status = "is idle"  

            return   
        else:
            starting_spot_x = self.person_pos_x
            starting_spot_y = self.person_pos_y 
            
            gameboard.board[self.person_pos_x][self.person_pos_y].stood_on = False 
            gameboard.board[self.person_pos_x][self.person_pos_y].stood_on_by = None 


            if self.person_pos_x < self.headed_toward[0]:
                self.person_pos_x += 1 
            
            if self.person_pos_y < self.headed_toward[1]:
                self.person_pos_y += 1 

            if self.person_pos_x > self.headed_toward[0]:
                self.person_pos_x -= 1 

            if self.person_pos_y > self.headed_toward[1]:
                self.person_pos_y -= 1 
            
            if gameboard.board[self.person_pos_x][self.person_pos_y].tileWalkable() == True:
                gameboard.board[self.person_pos_x][self.person_pos_y].stood_on = True 
                gameboard.board[self.person_pos_x][self.person_pos_y].stood_on_by = self 
            else:
                if gameboard.board[self.person_pos_x + 1][self.person_pos_y].tileWalkable() == True:
                    self.person_pos_x += 1 
                    gameboard.board[self.person_pos_x][self.person_pos_y].stood_on = True 
                    gameboard.board[self.person_pos_x][self.person_pos_y].stood_on_by = self 
                elif gameboard.board[self.person_pos_x -1][self.person_pos_y].tileWalkable() == True:
                    self.person_pos_x -= 1 
                    gameboard.board[self.person_pos_x][self.person_pos_y].stood_on = True 
                    gameboard.board[self.person_pos_x][self.person_pos_y].stood_on_by = self 
                elif gameboard.board[self.person_pos_x][self.person_pos_y + 1].tileWalkable() == True:
                    self.person_pos_y += 1 
                    gameboard.board[self.person_pos_x][self.person_pos_y].stood_on = True 
                    gameboard.board[self.person_pos_x][self.person_pos_y].stood_on_by = self 
                elif gameboard.board[self.person_pos_x][self.person_pos_y - 1].tileWalkable() == True:
                    self.person_pos_y -= 1 
                    gameboard.board[self.person_pos_x][self.person_pos_y].stood_on = True 
                    gameboard.board[self.person_pos_x][self.person_pos_y].stood_on_by = self 
                else:
                    self.person_pos_x = starting_spot_x
                    self.person_pos_y = starting_spot_y
                    gameboard.board[self.person_pos_x][self.person_pos_y].stood_on = True 
                    gameboard.board[self.person_pos_x][self.person_pos_y].stood_on_by = self 
            Universe.addAdventureLog(self.first_name + " is still on their way...")
            return 
    def hasReachedDestination(self):
        return self.person_pos_x == self.headed_toward[0] and self.person_pos_y == self.headed_toward[1]
    