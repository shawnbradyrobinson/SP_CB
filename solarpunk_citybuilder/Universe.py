# Universe keeps track of... 
# How many people there are in the game, currently 
# How much food your city has (Meal Inventory Items)
# All Inventory Items your community has gathered, 
# 
# Peace 
# Passion 
# How many buildings you have 
# How many days you've played 
# 
#
#
#
from TimeSystem import TimeSystem
from Buildings.HealthBuilding import HealthBuilding
from Buildings.Building import Building
from Person import Person
from names import names 
import pygame 
import random 
import math

## ========== SETTING UP LOTS OF STAT SYSTEMS FOR THE WORLD ========== ## 


persons_dict = { }
buildings_dict = { }

persons_sprites = [

"graphics/person_one.png",
"graphics/person_two.png",
"graphics/person_three.png",
"graphics/person_four.png",
"graphics/person_five.png",
"graphics/person_six.png"

]

Community_Peace = 50 
Community_Passion = 50 
Community_Level = 0
TEST_HEALTH_STAT = 0



#SHORT LOG CAN HOLD 6 
#LONG LOG CAN HOLD 26

adventure_logs = ["I wake to sleep, and take my waking slow",
                  "I feel my fate in what I cannot fear",
                  "I learn by going where I have to go",
                  " ",
                  "We think by feeling. What is there to know?",
                  "I hear my being dance from ear to ear",
                  "I wake to sleep, and take my waking slow",
                  " ",
                  "Of those so close beside me, which are you?",
                  "God bless the Ground! I shall walk softly there,",
                  "And learn by going where I have to go", 
                  " ", 
                  "Light takes the Tree; but who can tell us how?", 
                  "The lowly worm climbs up a winding stair;", 
                  "I wake to sleep, and take my waking slow", 
                  " ", 
                  "Great Nature has another thing to do", 
                  "To you and me; so take the lively air,", 
                  "And, lovely, learn by going where to go", 
                  " ", 
                  "This shaking keeps me steady. I should know", 
                  "What falls away is always. And is near.", 
                  "I wake to sleep, and take my waking slow", 
                  "I learn by going where I have to go.",  
                  "- Theodore Roethke",
                  " ------------------------------ "] 



## =========== INITIALIZATIONS ====================================== ## 


@staticmethod
def initPersons(starting_amount = 10):
    for i in range(starting_amount):
        rand_roll = int(random.uniform(0,1000))
        rr_two = math.floor(random.uniform(0,6))
        new_person = Person(names[rand_roll])
        persons_dict[new_person.person_name] = new_person 
        new_person.surface_sprite = pygame.image.load(persons_sprites[rr_two]).convert_alpha()
    pass 

    #print(persons_dict)






## ========= PERSON STUFF ================================= ## 
@staticmethod
def newPersonBorn():
    #age = 0
    #stats low 
    pass

@staticmethod
def newPersonArrives():
    #rand roll stats and stuff
    pass

@staticmethod 
def getTotalPersonAmount() -> int:
    return len(persons_dict)






## ======== BUILDING STUFF ============================ ## 
@staticmethod
def initBuildings() -> None:
    hb = HealthBuilding()
    buildings_dict["hb"] = hb 
    print(buildings_dict)
    
    pass 



@staticmethod 
def newBuilding(is_to_be_built) -> None:
    #is_to_be_built should match the name of a building type for the dictionary, so we can create the object and add it in there. 
    pass 


@staticmethod 
def worldEffects(TS: TimeSystem) -> None:
    #for each building in the world, run its effect check 
    #for now, there's just the one buidling lol 
    
    for i in buildings_dict.keys():
        buildings_dict[i].effect(TS)
    
    
    pass 


## ======== FOOD STUFF ======================== ##
@staticmethod
def getFoodStatusString() -> str:
    return "teststeady"




# ============ PEACE & PASSION STUFF ================= ##
@staticmethod
def getPeaceLevel() -> int:
    return Community_Peace


# ========== CITY LEVEL STUFF ======================== ##
@staticmethod
def getCommunityLevel() -> int:
    return Community_Level


# =========== ADVENTURE LOG STUFF ================== ## 
@staticmethod
def addAdventureLog(new_log: str): 
    for i in range(len(adventure_logs)-1):
        adventure_logs[i] = adventure_logs[i+1]
    adventure_logs[len(adventure_logs)-1] = new_log 
    pass 