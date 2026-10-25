import Universe
import pygame 
from LayerTypeIs import LayerTypeIs
from TileActionIs import TileActionIs
import random
#from Person import Person 


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
        self.avaiable_action = False 
        self.actions_resolved = True 
        self.tile_actions = [TileActionIs.EXPLORE_AND_MEADER]

        pass

    def refreshExternal(self):
        self.external = self.layers[len(self.layers)-1]
    
    def render(self):
        match(self.external):
           
           
           #TIER N 
           
            case LayerTypeIs.BEDROCK:
                self.image = pygame.image.load("graphics/bedrock.png").convert_alpha()
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
                self.image = pygame.image.load("graphics/iron_ore.png").convert_alpha()
                self.setTileActions(self.external)
            case LayerTypeIs.COAL_ORE:
                self.image = pygame.image.load("graphics/coal_ore.png").convert_alpha()
                
            case LayerTypeIs.OCEAN_VERY_DEEP:
                self.image = pygame.image.load("graphics/ocean_verydeep.png").convert_alpha()
                self.walkable = True  
                
            case LayerTypeIs.DIRT_HOLE_VERY_DEEP:
                self.image.fill("brown3")
                self.walkable = False 
                
    def addTileLayer(self, tile_layer: LayerTypeIs):
        self.layers.append(tile_layer)
        self.refreshExternal()

    def resetTileActions(self):
        self.tile_actions.clear()
        self.tile_actions.append(TileActionIs.EXPLORE_AND_MEADER)


    def getTileActions(self, tile_person) -> list:
        self.resetTileActions()
        match(self.external):
            case LayerTypeIs.SHORT_GRASS:
                self.tile_actions.append(TileActionIs.DIG_HOLE)

            case LayerTypeIs.TREE:
                if tile_person.personal_inventory.items["tools"]["standard_axe"] >= 1:
                    self.tile_actions.append(TileActionIs.CHOP_TREE)
                else:
                    pass

                self.tile_actions.append(TileActionIs.CLIMB_TREE)
            
            case LayerTypeIs.FOG:
                self.tile_actions.append(TileActionIs.CLEAR_FOG)
            
            # TIER 1 
            case LayerTypeIs.LAKE_SHALLOW:
                # eventually -- if person.has fishing rod == true then show fishing rod option
                self.tile_actions.append(TileActionIs.FISH_WITH_HANDS)

            case LayerTypeIs.OCEAN_SHALLOW:
                self.tile_actions.append(TileActionIs.FISH_WITH_HANDS)

            case LayerTypeIs.POND:
                self.tile_actions.append(TileActionIs.FISH_WITH_HANDS)


            # TIER 3 
            case LayerTypeIs.IRON_ORE:
                self.tile_actions.append(TileActionIs.MINE_IRON_ORE)
            
            case LayerTypeIs.COAL_ORE:
                self.tile_actions.append(TileActionIs.MINE_CORE_ORE)
        
            case ___:
                return self.tile_actions
        return self.tile_actions



# ============ BEWARE, YE WHO ENTER ============== # 



    def takeAction(self, tile_action: TileActionIs, tile_person):
        #Proficiency Calcs 
        ##OVERALL##
        ovr_prof_conv = 0 
        total_turns_toact = 0 

        


        ##OTHER PROFICIENCIES TO COME...## 




        match(tile_action):
            case TileActionIs.EXPLORE_AND_MEADER:
                #Let's do some sort of drop table, where we pass in the external tile type here 
                
                pass

            case TileActionIs.CHOP_TREE:
                self.actions_resolved = False 
                #This part can probably get generalized 
                if tile_person.overall_proficiency <= 24:
                    ovr_prof_conv = 2
                elif tile_person.overall_proficiency <= 49:
                    ovr_prof_conv = 1
                elif tile_person.overall_proficiency <= 74:
                    ovr_prof_conv = 0 
                else:
                    ovr_prof_conv = -1 

                if tile_person.currently_delegated_toact == False:
                    tile_person.total_action_turns = 3 + ovr_prof_conv
                    tile_person.current_action_turns = 0 
                    tile_person.currently_delegated_toact = True

                else:
                    pass
                
                tile_person.person_status = "chopping a tree for " + str(tile_person.current_action_turns) + "more turns"
                Universe.addAdventureLog(tile_person.first_name + "is chopping a tree for " +str(tile_person.total_action_turns - tile_person.current_action_turns) + "more turns")
                if tile_person.action_finished == True:
                    #This part can probably get generalized into a way to set parameters for turn_amounts 

                    flipped_conv = ovr_prof_conv * -1 

                    bonus_wood = random.uniform((0 + flipped_conv), + (3 + flipped_conv))
                    wood_added = random.uniform(5, 15) + bonus_wood 
                    Universe.Community_Inventory.items["materials"]["oak_planks"] += wood_added
                    Universe.addAdventureLog(tile_person.first_name + "chopped down the tree, received " + str(wood_added) + " oak wood planks")

                    ## THIS SHOULD BE GENERALIZED ## 
                    tile_person.currently_delegated_toact = False 
                    tile_person.current_action_turns = 0 
                    tile_person.total_action_turns = 0 
                    ## ========================== ## 
                    self.layers.pop()
                    self.refreshExternal()
                    self.render()
                    self.actions_resolved = True 
                pass

            case TileActionIs.MINE_STONE:
                pass

            case TileActionIs.FISH_WITH_HANDS:
                pass

            case TileActionIs.CLEAR_FOG:
                pass

            case TileActionIs.MINE_IRON_ORE:
                pass

            case TileActionIs.MINE_CORE_ORE:
                pass

            case TileActionIs.DIG_HOLE:
                pass
            
            case TileActionIs.FISH_WITH_ROD:
                pass 
            
            case TileActionIs.CLIMB_TREE:
                pass 


            case __:
                print("ERROR -- UNMATCHED TILE ACTION -> Tile.py ")
                return 
        return 


    def tileWalkable(self) -> bool:
        return self.walkable  