import Entity as Entity 
import Person as Person 


class Building(Entity):
    "Generic starting point for all building types"
    def __init__(self, building_name: str, height: int, width: int, materials_needed: dict):
        Entity.Entity.__init__(self, building_name)
        self.height = height
        self.width = width
        self.materials_needed = materials_needed
        self.person_capacity = 5 
        self.person_slots = [] #a list of objects? or a dict? 


    #Placeholder for any given building's "thing" that happens on continuous update 
    # so then in the game loop we can just have a class that says "for each building, run building.effect()"
    def effect():
        pass 

    def canConstruct() -> bool:
        #if Player.inventory includes stuff in the materials_needed dict, then true
        return True 

    pass

    def addPerson(self, person: Person):
        if len(self.person_slots) >= self.person_capacity:
            print("BUILDING ALREADY FULL")
            return 
        else:
            self.person_slots.append(person)
            return 
        
    
             
