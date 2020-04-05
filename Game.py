import pygame
from Player import Player

#game class
class Game:
    
    def __init__(self):
        
        #load player
        self.player = Player()
        self.pressed={}

