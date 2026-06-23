import pygame as pygame 
import Entity as Entity 
import EntitySprite as EntitySprite 
import TimeSystem 
import Universe 

from Gamestates.GamestateIs import GamestateIs
from Gamestates.MainMenu import MainMenu
from Gamestates.Observing import Observing

class Game: 
    
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("SOLAR PUNK CITY BUILDER")
        self.clock = pygame.time.Clock()
        self.dt = 0 
        self.TimeSys = TimeSystem.TimeSystem()
        self.current_gamestate = GamestateIs.MAIN_MENU

    def run(self):
        
    
        
        test_entity = Entity.Entity("first entity")
        test_entity_sprite = pygame.sprite.GroupSingle()
        test_entity_sprite.add(EntitySprite.EntitySprite(test_entity))
        
        
        second_entity = Entity.Entity("second!")
        second_entity_sprite = pygame.sprite.GroupSingle()
        second_entity_sprite.add(EntitySprite.EntitySprite(second_entity, "health_building_1", 300, 300))


        
        Universe.initBuildings()

        MAIN_MENU = MainMenu()
        OBSERVING = Observing()


        while True:
            
            match self.current_gamestate:
                case GamestateIs.MAIN_MENU:
                    MAIN_MENU.Reset()
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            exit()


                        keys = pygame.key.get_pressed()

                        MAIN_MENU.handleKeyInputs(keys)
                    
                    MAIN_MENU.drawDisplay(self.display_surface)
                    self.current_gamestate = MAIN_MENU.getInternalState()
                    pass

                case GamestateIs.OBSERVING:
                    OBSERVING.Reset()
                    # event loop 
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            exit()
                
                        keys = pygame.key.get_pressed()
                        OBSERVING.handleKeyInputs(keys, self.TimeSys)
                   
                    OBSERVING.drawDisplay(self.display_surface, self.TimeSys)
                    
                    self.TimeSys.nextInstant()
                    self.TimeSys.TickTickTick()
                    Universe.worldEffects(self.TimeSys)

                    self.current_gamestate = OBSERVING.getInternalState()
                    pass

                case GamestateIs.SETTINGS:
                    pass

                case GamestateIs.JUKEBOX:
                    pass

                case GamestateIs.PLACING:
                    pass

                case GamestateIs.DELGATING:
                    pass

                case __:
                    self.current_gamestate = GamestateIs.MAIN_MENU



            # test_entity_sprite.draw(self.display_surface)
            # test_entity_sprite.update()
                
            # second_entity_sprite.draw(self.display_surface)
            # second_entity_sprite.update()

            pygame.display.update()
                
            self.dt = self.clock.tick(60) / 1000 #limits FPS to 60


            
        
            
game = Game()
game.run()