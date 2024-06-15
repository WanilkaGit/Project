import pygame as pg
from sonya import *

pg.init()

hero_lives = 3

WHITE = (255, 255, 255)


screen = pg.display.set_mode()
font = pg.font.SysFont('Aharoni', 65, True, False) 
text_game_over = font.render("You lose", True, (51, 225, 249)) 

text_life = font.render('Life: ' + str(hero_lives), True, (0,0,0))

def lose(window):
    global scene
    screen.blit(text_game_over, [20, 170])
    scene = 6
    window.blit(restart_btn)
    window.blit(exit_to_main)
    



    

