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
            case LayerTypeIs.BEDROCK:
                self.image.fill("Grey10")
            case LayerTypeIs.LAKE_SHALLOW:
                self.image.fill("blue") 
            case LayerTypeIs.SHORT_GRASS:
                self.image.fill("green")


