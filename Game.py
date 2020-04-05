import pygame
from Player import Player
from Monster import Monster

#game class
class Game:
    
    def __init__(self):
        
        #load player
        self.player = Player()
        self.pressed={}
        self.all_monsters=pygame.sprite.Group()
        self.spawnMonster()
        
    def spawnMonster(self):
        #load Monster
        monster= Monster()
        self.all_monsters.add(monster)

