import pygame


#Monster Class
class Monster(pygame.sprite.Sprite):
    
    def __init__(self,Game, Wscreen, Hscreen):
        
        super(Monster, self).__init__()
        self.game=Game
        self.health=100;
        self.maxhealth=100
        self.attack=10
        self.velocity=1
        self.image=pygame.image.load('assets/virus.png')
        self.image=pygame.transform.scale(self.image, (83,83))
        self.rect=self.image.get_rect()
        self.rect.x=Wscreen
        self.rect.y=Hscreen-115
    
    def forward(self):
        
        #check if monster are not in collision with any Player
        if not self.game.checkCollision(self, self.game.all_players):
            self.rect.x-=self.velocity
            
    def die(self):
        
        if self.game.checkCollision(self, self.game.player.right_projectile):
            self.game.all_monsters.remove(self)
