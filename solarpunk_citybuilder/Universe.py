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


## ========== SETTING UP LOTS OF STAT SYSTEMS FOR THE WORLD ========== ## 


persons_dict = { }
buildings_dict = { }



Community_Peace = 50 
Community_Passion = 50 
Community_Level = 0
TEST_HEALTH_STAT = 0


## =========== INITIALIZATIONS ====================================== ## 


@staticmethod
def initPersons(starting_amount = 10):
    pass 







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