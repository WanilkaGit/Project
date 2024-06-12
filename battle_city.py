import pygame as pg

from maxym import *
from sonya import *
from ivan import *
from kostya import *

pg.init()
pg.mixer.init()

window = pg.display.set_mode((0, 0), pg.FULLSCREEN)
pg.display.set_caption('Battle City')
back = pg.transform.scale(pg.image.load('fon1.jpg'), (1500, 1000))  #завантажуєемо картинку фона і розтягємо її у рзміри екрана
game = True

how_to_play_btn = Button(630, 200, 200, 80, font, 'How to play', (100, 10, 10))
play_btn = Button(630, 300, 200, 80, font, 'Play', (100, 10, 10))
setting_btn = Button(630, 400, 200, 80, font, 'Settings', (100, 10, 10))

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
            if setting_btn.is_pressed(event.pos):
                print(True, 'setting working')
                setting()

            if how_to_play_btn.is_pressed(event.pos):
                print(True, 'rule working')
                display_rules(window)

            if play_btn.is_pressed(event.pos):
                print(True, 'play working')
                start_pos()


    pg.display.update()
pg.quit()
