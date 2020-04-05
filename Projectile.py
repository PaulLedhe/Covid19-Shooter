import pygame

#projectile class
class Projectile(pygame.sprite.Sprite):
    
    def __init__(self,player, positionx):
        
        super(Projectile, self).__init__()
        self.velocity=5
        self.player=player
        self.image=pygame.image.load('assets/projectile.png')
        self.image=pygame.transform.scale(self.image, (60,52))
        self.rect=self.image.get_rect()
        self.rect.x=player.rect.x + positionx
        self.rect.y=player.rect.y + 91
    
    def remove(self, a):
        if a == True :
            
            self.player.right_projectile.remove(self)
        else :
            self.player.left_projectile.remove(self)
    
    def moveRight(self, screen):
        
        self.image=pygame.image.load('assets/projectile/projectileR.png')
        
        self.rect.x+= self.velocity
        
        if self.rect.x > screen :
            self.remove(True)
            
        #check if projectile hit a monster
        if self.player.game.checkCollision(self, self.player.game.all_monsters):
            self.remove(True)

            
    def moveLeft(self):
        
        self.image=pygame.image.load('assets/projectile/projectileL.png')

        self.rect.x -= self.velocity
        
        if self.rect.x < 0 :
            self.remove(False)
        
        if self.player.game.checkCollision(self, self.player.game.all_monsters):
            self.remove(False)
            
        