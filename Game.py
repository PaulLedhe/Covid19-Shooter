import pygame
from Player import Player
from Monster import Monster
from matplotlib.pyplot import spring
from IPython.utils._tokenize_py2 import group

#game class
class Game:
    
    def __init__(self,Wscreen, Hscreen):
        
        #load player
        self.all_players=pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        self.pressed={}
        self.all_monsters=pygame.sprite.Group()
        self.spawnMonster(Wscreen, Hscreen)
        
    def spawnMonster(self,Wscreen, Hscreen):
        #load Monster
        monster= Monster(self,Wscreen, Hscreen)
        self.all_monsters.add(monster)
        
    def checkCollision(self, sprite, group):
        #check collition between two entities
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)
        

