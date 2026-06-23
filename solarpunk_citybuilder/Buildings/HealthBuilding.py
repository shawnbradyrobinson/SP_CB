from Buildings.Building import Building 
from Person import Person
from Entity import Entity 
from TimeSystem import TimeSystem
import Universe 



health_building_materials = {
    "oak_planks": 5,
    "bricks": 5
}


class HealthBuilding(Building):
    def __init__(self):
        Building.__init__(self, "health_building", 50, 50, health_building_materials)
        self.tracked_hours = 0 

    def effect(self, TS: TimeSystem):
        if TS.getHours() != self.tracked_hours:
            self.tracked_hours = TS.getHours()
            print("health building effect")
            Universe.TEST_HEALTH_STAT += 1 
             
        pass

