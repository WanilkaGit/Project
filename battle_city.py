import pygame as pg
from oleksii import *
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

scene = 0

while game:
    window.blit(back, (0,0))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            game = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                game = False
                        
        if event.type == pg.MOUSEBUTTONDOWN:
            if setting_btn.is_pressed(event.pos):
                print(True, 'setting working')
                scene = 2

            if how_to_play_btn.is_pressed(event.pos):
                print(True, 'rule working')
                scene = 3

            if play_btn.is_pressed(event.pos):
                print(True, 'play working')
                scene = 1
                
    if scene == 0:
        main_menu()
    elif scene == 1:
        start_pos()
        for item in items:
            window.blit(item.image, (item.rect.x, item.rect.y))
    elif scene == 2:
        setting()
    elif scene == 3:
        display_rules(window)
    

    if hero_lives == 0:
        lose()


    pg.display.update()
pg.quit()
