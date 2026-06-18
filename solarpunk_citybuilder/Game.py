import pygame as pygame 
import Entity as Entity 
import EntitySprite as EntitySprite 
import TimeSystem 
import Universe 

class Game: 
    
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("SOLAR PUNK CITY BUILDER")
        self.clock = pygame.time.Clock()
        self.dt = 0 
        self.TimeSys = TimeSystem.TimeSystem()

    def run(self):
        
        test_surface = pygame.Surface((1200,800)).convert_alpha()
        test_surface.fill("light blue")
        
    
        
        test_entity = Entity.Entity("first entity")
        test_entity_sprite = pygame.sprite.GroupSingle()
        test_entity_sprite.add(EntitySprite.EntitySprite(test_entity))
        
        
        second_entity = Entity.Entity("second!")
        second_entity_sprite = pygame.sprite.GroupSingle()
        second_entity_sprite.add(EntitySprite.EntitySprite(second_entity, "health_building_1", 300, 300))



        time_font = pygame.font.Font(None, 24)
        time_string = "N/A"
        time_display_surface = time_font.render(time_string, False, "Black")
        counter = 0 
        delta_set = 1 
        
        Universe.initBuildings()


        while True:
            # event loop 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                
                keys = pygame.key.get_pressed()

                if keys[pygame.K_RIGHT]:
                    self.TimeSys.changeDelta(self.TimeSys.delta * 2)
                
                if keys[pygame.K_LEFT]:
                    self.TimeSys.changeDelta(self.TimeSys.delta * .5)

                if keys[pygame.K_DOWN]:
                    if self.TimeSys.delta == 0:
                        self.TimeSys.changeDelta(1)
                    else: 
                        self.TimeSys.changeDelta(0)

                if keys[pygame.K_q]:
                    pygame.quit()
                    exit()
                
            self.display_surface.blit(test_surface, (0,0))

            test_entity_sprite.draw(self.display_surface)
            test_entity_sprite.update()
                
            second_entity_sprite.draw(self.display_surface)
            second_entity_sprite.update()

            self.TimeSys.nextInstant()
            self.TimeSys.TickTickTick()

            test_health_string = "HEALTH STAT UPDATED ON THE HOUR: " + str(Universe.TEST_HEALTH_STAT)
            ths_display_surface = time_font.render(test_health_string, False, "Black")
            self.display_surface.blit(ths_display_surface, (250, 250))



            instants_string = str(self.TimeSys.counter)
            time_display_surface = time_font.render(instants_string, False, "Black")
            self.display_surface.blit(time_display_surface, (1000, 15))

            hours_string = str(self.TimeSys.getHours())
            hours_display_surface = time_font.render(hours_string, False, "Blue")
            self.display_surface.blit(hours_display_surface, (1000, 30))

            days_string = str(self.TimeSys.getDays())
            days_display_surface = time_font.render(days_string, False, "Blue")
            self.display_surface.blit(days_display_surface, (1000, 45))

            months_string = str(self.TimeSys.getMonths())
            months_display_surface = time_font.render(months_string, False, "Red")
            self.display_surface.blit(months_display_surface, (1000, 60))


            years_string = str(self.TimeSys.getYears())
            years_display_surface = time_font.render(years_string, False, "Green")
            self.display_surface.blit(years_display_surface, (1000, 75))




            Universe.worldEffects(self.TimeSys)
            pygame.display.update()
                
            self.dt = self.clock.tick(60) / 1000 #limits FPS to 60


            
        
            
game = Game()
game.run()