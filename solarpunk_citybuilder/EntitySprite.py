import pygame 
import Entity as Entity 



class EntitySprite(pygame.sprite.Sprite):
    "A generalized sprite container for manipulating entity data graphically on the pygame window"
    def __init__(self, entity_object: Entity, image_name = "health_building_1", height = 50, width = 50):
        pygame.sprite.Sprite.__init__(self)
        
        #connecting the sprite container with the entity data stored elsewhere 
        self.entity_object = entity_object 
        
       # self.fill_color = fill_color
        self.image = pygame.image.load("graphics/"+image_name+".png").convert_alpha()
        #self.image.fill(self.fill_color)
        self.rect = self.image.get_rect()
        self.label = pygame.font.Font(None, 20)
        label_surface = self.label.render(entity_object.entity_name, False, "white")
        self.image.blit(label_surface)
    
    def update(self):
        self.inputs()
    
    def inputs(self):
        keys = pygame.key.get_pressed()
        # if self.fill_color == "orange":
        #     if keys[pygame.K_w]:
        #         self.rect.y -= 50
        #     if keys[pygame.K_s]:
        #         self.rect.y += 50 
        #     if keys[pygame.K_a]:
        #         self.rect.x -= 50 
        #     if keys[pygame.K_d]:
        #         self.rect.x += 50 