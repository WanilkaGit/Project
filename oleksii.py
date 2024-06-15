import pygame as pg

pg.init()

hero_lives = 3

WHITE = (255, 255, 255)


screen = pg.display.set_mode()
font = pg.font.SysFont('Aharoni', 65, True, False) 
text_game_over = font.render("You lose", True, (51, 225, 249)) 
text_game_over1 = font.render("Press r to restart", True, (51, 225, 249)) 
text_life = font.render('Life: ' + str(hero_lives), True, (0,0,0))

def lose():
    global scene
    screen.blit(text_game_over, [20, 170])
    screen.blit(text_game_over1, [20, 200])
    scene = 6
    
if hero_lives == 0:
    game = False        
else:
    pass
    
if game == False:
    window.blit(text_game_over, [600, 280])
    window.blit(text_game_over1, [600, 320])
    pg.mixer.music.play()
    window.blit(restart_btn)
    window.blit(exit_to_main)
else:
    pass

text_lives = font.render("Score: " + str(hero_lives), True, WHITE)

    

