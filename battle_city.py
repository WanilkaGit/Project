import pygame as pg

pg.init()
# pg.mixer.init()


hero_lives = 1


screen = pg.display.set_mode()
font = pg.font.SysFont('TH SarabunPSK Bold', 65, True, False) 
text_game_over = font.render("You lose", True, (51, 225, 249)) 
text_game_over1 = font.render("Press ESC to restart", True, (51, 225, 249)) 


display = pg.display.set_mode((0, 0), pg.FULLSCREEN)
pg.display.set_caption('Battle City')
# pg.mixer.music.load('lose.ogg')

game = True

while game:
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            game = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                game = False

    if hero_lives == 0:
        game = False
    else:
        pass
    
    if game == False:
        screen.blit(text_game_over, [20, 170])
        screen.blit(text_game_over1, [20, 210])
        pg.mixer.music.play()
    else:
        pass



    pg.display.update()
