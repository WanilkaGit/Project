import pygame as pg
from maxym import *
from ivan import *
from sonya import main_menu, setting, push_btn

pg.init()
pg.mixer.init()

window = pg.display.set_mode((0, 0), pg.FULLSCREEN)
pg.display.set_caption('Battle City')
back = pg.transform.scale(pg.image.load('fon1.jpg'), (1500, 1000))  #завантажуєемо картинку фона і розтягємо її у рзміри екрана
game = True

while game:
    window.blit(back, (0,0))
    main_menu()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            game = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                game = False
                        
        if event.type == pg.MOUSEBUTTONDOWN:
            push_btn()

    pg.display.update()
pg.quit()
