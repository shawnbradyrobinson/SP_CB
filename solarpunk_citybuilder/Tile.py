import Universe
import pygame 
from LayerTypeIs import LayerTypeIs

class Tile:
    def __init__(self, square_dimension_px = 50):
        self.square_dimesion_px = square_dimension_px
        self.layers = [LayerTypeIs.BEDROCK]
        self.stood_on = False 
        self.stood_on_by = None #Person object that is on this Tile 
        self.walkable = True 
        self.external = self.layers[len(self.layers)-1]
        self.image = pygame.Surface((square_dimension_px, self.square_dimesion_px)).convert_alpha()
        self.image.fill("Yellow")
        pass

    def refreshExternal(self):
        self.external = self.layers[len(self.layers)-1]
    
    def render(self):
        match(self.external):
           
           
           #TIER N 
           
            case LayerTypeIs.BEDROCK:
                self.image.fill("Grey10")
                self.walkable = False 

            # TIER 0 
            case LayerTypeIs.SHORT_GRASS:
                self.image = pygame.image.load("graphics/short_grass.jpg").convert_alpha()
            
            case LayerTypeIs.TALL_GRASS:
                self.image = pygame.image.load("graphics/tall_grass_1.png").convert_alpha()
            
            case LayerTypeIs.TREE:
                self.image = pygame.image.load("graphics/tree_typeone.png").convert_alpha()
                self.walkable = True 
            
            
            
            case LayerTypeIs.FOG:
                self.image.fill("gray60")
                self.walkable = True 
            
            # TIER 1 
            case LayerTypeIs.LAKE_SHALLOW:
                self.image = pygame.image.load("graphics/lake_shallow.jpg").convert_alpha()
                self.walkable = True 

            case LayerTypeIs.OCEAN_SHALLOW:
                self.image = pygame.image.load("graphics/ocean_shallow.png")
                self.walkable = True 
            
            case LayerTypeIs.DIRT_HOLE_SHALLOW:
                self.image = pygame.image.load("graphics/dirt_shallow.png").convert_alpha()

            case LayerTypeIs.POND:
                self.image = pygame.image.load("graphics/pond.png").convert_alpha()
                self.walkable = False 





            # TIER 2 

            case LayerTypeIs.LAKE_DEEP:
                self.image = pygame.image.load("graphics/lake_deep.png").convert_alpha()
                self.walkable = False 

            case LayerTypeIs.OCEAN_DEEP:
                self.image = pygame.image.load("graphics/ocean_deep.png").convert_alpha()
                self.walkable = False 
            
            case LayerTypeIs.DIRT_HOLE_DEEP:
                self.image = pygame.image.load("graphics/dirt_deep.png").convert_alpha()
                self.walkable = False 


            # TIER 3 
            case LayerTypeIs.IRON_ORE:
                self.image.fill("silver")
            
            case LayerTypeIs.COAL_ORE:
                self.image.fill("black")

            case LayerTypeIs.OCEAN_VERY_DEEP:
                self.image = pygame.image.load("graphics/ocean_verydeep.png").convert_alpha()
                self.walkable = True  
            
            case LayerTypeIs.DIRT_HOLE_VERY_DEEP:
                self.image.fill("brown3")
                self.walkable = False 

    def addTileLayer(self, tile_layer: LayerTypeIs):
        self.layers.append(tile_layer)
        self.refreshExternal()

    def tileWalkable(self) -> bool:
        return self.walkable  