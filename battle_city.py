import pygame as pg

pg.init()

display = pg.display.set_mode((0, 0), pg.FULLSCREEN)
pg.display.set_caption('Battle City')

game = True

while game:
    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                game = False


    pg.display.update()
    

pg.quit()