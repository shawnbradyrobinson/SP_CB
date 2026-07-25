import pygame as pygame 
import Entity as Entity 
import EntitySprite as EntitySprite 
import TimeSystem 
import MusicSystem 
import Universe 
from Gameboard import Gameboard 

from Gamestates.GamestateIs import GamestateIs
from Gamestates.MainMenu import MainMenu
from Gamestates.Observing import Observing
from Gamestates.Jukebox import Jukebox
from Gamestates.Settings import Settings
from Gamestates.NotDone import NotDone
from Gamestates.Placing import Placing 
from Gamestates.NewGame import NewGame
from Gamestates.People import People 
from Gamestates.Credits import Credits


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
        
    
        
        #test_entity = Entity.Entity("first entity")
        #test_entity_sprite = pygame.sprite.GroupSingle()
        #test_entity_sprite.add(EntitySprite.EntitySprite(test_entity))
        
        
        #second_entity = Entity.Entity("second!")
        #second_entity_sprite = pygame.sprite.GroupSingle()
        #second_entity_sprite.add(EntitySprite.EntitySprite(second_entity, "health_building_1", 300, 300))


        
        Universe.initBuildings()
        Universe.initPersons(100)

        GAMEBOARD = Gameboard()
        # for j in range(100):
        #     for i in range(100):
        #         GAMEBOARD.board[i][j].render()

        
        MAIN_MENU = MainMenu()
        NEW_GAME = NewGame(GAMEBOARD)
        OBSERVING = Observing(GAMEBOARD)
        PEOPLE = People()
        JUKEBOX = Jukebox()
        SETTINGS = Settings()
        NOTDONE = NotDone()
        PLACING = Placing()
        CREDITS = Credits()

        MusicSystem.play_soundtrack()
        self.latest_hour = 0 
        while True:
            
            match self.current_gamestate:
                case GamestateIs.MAIN_MENU:
                    MAIN_MENU.Reset()
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            exit()


                        keys = pygame.key.get_just_pressed()

                        MAIN_MENU.handleKeyInputs(keys)
                    
                    MAIN_MENU.drawDisplay(self.display_surface)
                    self.current_gamestate = MAIN_MENU.getInternalState()
                    pass

                case GamestateIs.OBSERVING:
                    OBSERVING.Reset()
                    OBSERVING.handleMusic()  
                    # event loop 
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            exit()
                
                        keys = pygame.key.get_pressed()
                        OBSERVING.handleKeyInputs(keys, self.TimeSys)
                   
                    OBSERVING.drawDisplay(self.display_surface, self.TimeSys)
                    
                    # if OBSERVING.grid_on == True:
                    #     OBSERVING.drawGrid(self.display_surface)
                    # else:
                    #     pass
                    

                    self.TimeSys.nextInstant()
                    self.TimeSys.TickTickTick()
                    Universe.worldEffects(self.TimeSys)


                    #WALKING SOMEWHERE EACH HOUR 
                    if self.TimeSys.getHours() > self.latest_hour:
                        for person in Universe.persons_dict.keys():
                            peep = Universe.persons_dict[person]
                            if peep.currently_delegated == True:
                                peep.continue_guided_walk(GAMEBOARD)
                            else:
                                peep.random_walk(GAMEBOARD)
                            
                        self.latest_hour = self.TimeSys.getHours()




                    self.current_gamestate = OBSERVING.getInternalState()
                    pass

                case GamestateIs.SETTINGS:
                    SETTINGS.Reset()
                    SETTINGS.handleMusic()
                    # event loop 
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            exit()
                        keys = pygame.key.get_pressed()
                        SETTINGS.handleKeyInputs(keys)

                    SETTINGS.drawDisplay(self.display_surface)
                    self.current_gamestate = SETTINGS.getInternalState()
                    pass 

                case GamestateIs.JUKEBOX:
                    JUKEBOX.Reset()
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            exit()

                        keys = pygame.key.get_pressed()
                        JUKEBOX.handleKeyInputs(keys)

                        JUKEBOX.drawDisplay(self.display_surface)         
                        self.current_gamestate = JUKEBOX.getInternalState()           

                case GamestateIs.PLACING:
                    PLACING.Reset()
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            exit()

                        keys = pygame.key.get_pressed()
                        PLACING.handleKeyInputs(keys)
                        PLACING.drawDisplay(self.display_surface, OBSERVING.test_surface , self.TimeSys)
                        self.current_gamestate = PLACING.getInternalState()


                case GamestateIs.PEOPLE:
                    PEOPLE.Reset()
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            exit()

                        keys = pygame.key.get_pressed()
                        PEOPLE.handleKeyInputs(keys)
                        PEOPLE.drawDisplay(self.display_surface)
                        self.current_gamestate = PEOPLE.getInternalState()

                case GamestateIs.NEW_GAME:
                    NEW_GAME.Reset()
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            exit()
                        
                        keys = pygame.key.get_pressed()
                        NEW_GAME.handleKeyInputs(keys)
                        NEW_GAME.drawDisplay(self.display_surface)
                        self.current_gamestate = NEW_GAME.getInternalState() 
                    pass

                case GamestateIs.CREDITS:
                    CREDITS.Reset()
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            exit()
                        keys = pygame.key.get_pressed()
                        CREDITS.handleKeyInputs(keys)
                        CREDITS.drawDisplay(self.display_surface)
                        self.current_gamestate = CREDITS.getInternalState()
                    pass     
                
                case GamestateIs.NOT_DONE:
                    NOTDONE.Reset()
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            exit()

                        keys = pygame.key.get_pressed()
                        NOTDONE.handleKeyInputs(keys)
                        NOTDONE.drawDisplay(self.display_surface)
                        self.current_gamestate = NOTDONE.getInternalState()
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