import pygame
from pygame.examples.mask import Sprite
from Game import Game
from pygame.constants import K_SPACE, K_a, K_e, K_LEFT, K_d

pygame.init()


#window
pygame.display.set_caption("covid-19 Shooter")
screen=pygame.display.set_mode((800, 480))

#load background
background=pygame.image.load('assets/hospital_room4.jpg')

#load game
game=Game(screen.get_width(),screen.get_height())

#loop which keep the window on (while running is True)
running=True
while running :
    
    #set window
    screen.blit(background, (0,0))
    
    #set player
    screen.blit(game.player.image, game.player.rect)
    
    #set player projectile
    game.player.right_projectile.draw(screen)
    game.player.left_projectile.draw(screen)
    
    #set Monsters
    game.all_monsters.draw(screen)
    
    #move player
    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x + game.player.rect.width < screen.get_width():
        game.player.moveRight()
    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 0:
        game.player.moveLeft()
        
    #move Monsters
    for monster in game.all_monsters:
        monster.forward()
        monster.die()
        
    #launch projectile
        #to the right side
    for projectile in game.player.right_projectile:
        projectile.moveRight(screen.get_width())
        
        #to the left side
    for projectile in game.player.left_projectile:
        projectile.moveLeft()
    
    #refresh screen
    pygame.display.flip()
     
    #if player close the window
    for event in pygame.event.get():
        #detect if user close the window
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("end game")
            
        #detect if the user releases a keyboard key
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key]= True
            
            #detect if the user press e (right side lauch)
            if event.key==K_d:
                game.player.lauchProjectileRight()

            #detect if the user press a (left side lauch)
            if event.key==K_a:
                game.player.lauchProjectileLeft()
                
        elif event.type == pygame.KEYUP:
            game.pressed[event.key]= False
   
        
        
        
        