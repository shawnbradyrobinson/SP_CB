import Entity as Entity 
import Inventory as Inventory

class Person(Entity):
    "Generic starting point for all persons"
    def __init__(self, person_name: str):
        Entity.Entity.__init__(self, person_name)
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
        self.personal_inventory = Inventory.Inventory()

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

    def changeOverallProficiency(self, new_ovr: int)
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