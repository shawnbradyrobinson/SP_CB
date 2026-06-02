import Entity as Entity 


class Building(Entity):
    "Generic starting point for all building types"
    def __init__(self, height: int, width: int, materials_needed: dict):
        Entity.Entity.__init__(self)
        self.height = height
        self.width = width
        self.materials_needed = materials_needed



    def effect():
        pass 

    def canConstruct() -> bool:
        #if Player.inventory includes stuff in the materials_needed dict, then true
        
        
        return True 





    pass