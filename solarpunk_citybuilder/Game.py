import pygame as pygame 
import Entity as Entity 
import EntitySprite as EntitySprite 
import TimeSystem 

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
        test_entity_sprite.add(EntitySprite.EntitySprite(test_entity, "green"))
        
        
        second_entity = Entity.Entity("second!")
        second_entity_sprite = pygame.sprite.GroupSingle()
        second_entity_sprite.add(EntitySprite.EntitySprite(second_entity, "orange", 300, 300))



        time_font = pygame.font.Font(None, 24)
        time_string = "N/A"
        time_display_surface = time_font.render(time_string, False, "Black")
        counter = 0 
        delta_set = 1 
        
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


            time_string = str(self.TimeSys.counter)
            time_display_surface = time_font.render(time_string, False, "Black")
            self.display_surface.blit(time_display_surface, (1000, 15))
                
            pygame.display.update()
                
            self.dt = self.clock.tick(60) / 1000 #limits FPS to 60


            
        
            
game = Game()
game.run()