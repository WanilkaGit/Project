import pygame as pg
from sonya import restart_btn, exit_to_main

pg.font.init()

WHITE = (255, 255, 255)

font = pg.font.SysFont('Aharoni', 65, True, False) 
text_game_over = font.render("You lose", True, (51, 225, 249)) 


def lose(window):
    window.blit(text_game_over, [20, 170])
    restart_btn.draw(window)
    exit_to_main.draw(window)
    



    

