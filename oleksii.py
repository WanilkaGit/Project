import pygame as pg

pg.init()

hero_lives = 3

WHITE = (255, 255, 255)


screen = pg.display.set_mode()
font = pg.font.SysFont('Aharoni', 65, True, False) 
text_game_over = font.render("You lose", True, (51, 225, 249)) 
text_game_over1 = font.render("Press r to restart", True, (51, 225, 249)) 


def lose():
    screen.blit(text_game_over, [20, 170])
    screen.blit(text_game_over1, [20, 200])
    

