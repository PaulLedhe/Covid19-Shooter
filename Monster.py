import pygame


#Monster Class
class Monster(pygame.sprite.Sprite):
    
    def __init__(self):
        
        super(Monster, self).__init__()
        self.health=100;
        self.maxhealth=100
        self.attack=10
        self.velocity=5
        self.image=pygame.image.load('assets/virus.png')
        self.image=pygame.transform.scale(self.image, (83,83))
        self.rect=self.image.get_rect()
        