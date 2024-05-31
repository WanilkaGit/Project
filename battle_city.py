import pygame as pg

pg.init()

FPS = 60

display = pg.display.set_mode((0, 0), pg.FULLSCREEN)
pg.display.set_caption('Battle City')

game = True

clock = pg.time.Clock()
while game:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            game = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                game = False


    pg.display.update()
    clock.tick(FPS)
    

pg.quit()