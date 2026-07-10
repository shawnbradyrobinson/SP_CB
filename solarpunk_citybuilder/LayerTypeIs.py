from enum import Enum, auto 

class LayerTypeIs(Enum):
    
    ## ===== TIER 0 ===== ## -- Things that are above ground  
    TREE = auto()
    TALL_GRASS = auto()
    SHORT_GRASS = auto()
    

    ## === RESIDENTIAL BUIDLING === ## 



    ## ============================= ## 


    ## === MEDICAL BUILDING === ##



    ## ============================= ## 



    ## === SCHOOLHOUSE === ##




    ## =============================== ## 
    
    
    
    ## TIER 1 ## -- Things in shallow ground or bordering surface and under 
    POND = auto()
    LAKE_SHALLOW = auto()
    OCEAN_SHALLOW = auto()
    DIRT_HOLE_SHALLOW = auto()

    ## TIER 2 ## -- Things in deep ground 
    LAKE_DEEP = auto()
    OCEAN_DEEP = auto()
    DIRT_HOLE_DEEP = auto()




    ## TIER 3 ## -- Things in critically deep ground 
    IRON_ORE = auto()
    COAL_ORE = auto()
    OCEAN_VERY_DEEP = auto()
    DIRT_HOLE_VERY_DEEP = auto()

    ## TIER N ## 
    BEDROCK = auto()




