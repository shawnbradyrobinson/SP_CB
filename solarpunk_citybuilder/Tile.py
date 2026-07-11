import Universe
import pygame 
from LayerTypeIs import LayerTypeIs

class Tile:
    def __init__(self, square_dimension_px = 50):
        self.square_dimesion_px = square_dimension_px
        self.layers = [LayerTypeIs.BEDROCK]
        self.stood_on = False 
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

            # TIER 0 
            case LayerTypeIs.SHORT_GRASS:
                self.image.fill("green")
            case LayerTypeIs.TALL_GRASS:
                self.image = pygame.image.load("graphics/tall_grass_1.png").convert_alpha()
            case LayerTypeIs.TREE:
                self.image.fill("goldenrod1")
            
            # TIER 1 
            case LayerTypeIs.LAKE_SHALLOW:
                self.image.fill("blue") 
            
            case LayerTypeIs.OCEAN_SHALLOW:
                self.image.fill("darkblue")
            
            case LayerTypeIs.DIRT_HOLE_SHALLOW:
                self.image.fill("brown1")


            # TIER 2 

            case LayerTypeIs.LAKE_DEEP:
                self.image.fill("dodgerblue3")
            
            case LayerTypeIs.OCEAN_DEEP:
                self.image.fill("blue4")
            
            case LayerTypeIs.Dirt_HOLE_DEEP:
                self.image.fill("brown2")


            # TIER 3 
            case LayerTypeIs.IRON_ORE:
                self.image.fill("silver")
            
            case LayerTypeIs.COAL_ORE:
                self.image.fill("black")

            case LayerTypeIs.OCEAN_VERY_DEEP:
                self.image.fill("darkslateblue")
            
            case LayerTypeIs.DIRT_HOLE_VERY_DEEP:
                self.image.fill("brown3")
