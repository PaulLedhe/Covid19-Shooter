import pygame
from Projectile import Projectile

#player class
class Player(pygame.sprite.Sprite):
    
    def __init__(self):
        super(Player, self).__init__()
        self.health=100;
        self.maxhealth=100
        self.attack=10
        self.velocity=5
        self.right_projectile=pygame.sprite.Group()
        self.left_projectile=pygame.sprite.Group()
        self.image=pygame.image.load('assets/player.png')
        self.rect = self.image.get_rect()
        self.rect.y=480-183-10
        
    def lauchProjectileRight(self):
        self.right_projectile.add(Projectile(self,70))
        
    def lauchProjectileLeft(self):
        self.left_projectile.add(Projectile(self,-30))
    
        
    def moveRight(self):
        self.rect.x +=self.velocity
        
    def moveLeft(self):
        self.rect.x -=self.velocity