import pygame as pg

pg.init()
pg.mixer.init()
hero_lives = 3

WHITE = (255, 255, 255)

screen = pg.display.set_mode()
font = pg.font.SysFont('Aharoni', 65, True, False) 
text_game_over = font.render("You lose", True, (51, 225, 249)) 
text_game_over1 = font.render("Press ESC to restart", True, (51, 225, 249)) 


display = pg.display.set_mode((0, 0), pg.FULLSCREEN)
pg.display.set_caption('Battle City')
pg.mixer.music.load('lose.ogg')


def lose():
    screen.blit(text_game_over, [20, 170])
    screen.blit(text_game_over1, [20, 200])
    pg.mixer.music.play()
    text = font.render("Score: " + str(hero_lives), True, WHITE)
