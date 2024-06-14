import pygame as pg
from oleksii import *
from maxym import *
from sonya import *
from ivan import *
from kostya import *

pg.init()
pg.font.init()
pg.mixer.init()


window = pg.display.set_mode((0, 0), pg.FULLSCREEN)
W, H = pg.display.Info().current_w, pg.display.Info().current_h

pg.display.set_caption('Battle City')
pg.display.set_icon(pg.image.load('assets\\textures\\fon1.jpg'))  #завантажуєемо фото іконки
back = pg.transform.scale(pg.image.load('assets\\textures\\fon1.jpg'), (W, H))  #завантажуєемо картинку фона і розтягємо її у рзміри екрана
game = True

how_to_play_btn = Button(630, 200, 200, 80, font, 'How to play', (100, 10, 10))
play_btn = Button(630, 300, 200, 80, font, 'Play', (100, 10, 10))
setting_btn = Button(630, 400, 200, 80, font, 'Settings', (100, 10, 10))
exit_btn = Button(630, 500, 200, 80, font, 'Exit', (100, 10, 10))

scene = 0

last_call_time = pg.time.get_ticks()
interval = 100

enemy = pg.image.load("assets\\textures\\player\\tank1.png")
bullet = pg.image.load("assets\\textures\\blocks\\bullet.png")
bullet_obj = Bullet(bullet, 3, damage = 2)
enemy_tank1 = Enemy(enemy, 2, 1, 2, 1, 2, bullet_obj, items)
enemys = EnemySpawner([enemy_tank1, enemy_tank1], ((200, 50), (650,50)))

while game:
    window.blit(back, (0,0))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            game = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                game = False         
        if event.type == pg.MOUSEBUTTONDOWN:
            if scene == 0:
                if exit_btn.is_pressed(event.pos):
                    game = False 

                if setting_btn.is_pressed(event.pos):
                    scene = 2

                if how_to_play_btn.is_pressed(event.pos):
                    scene = 3

                if play_btn.is_pressed(event.pos):
                    scene = 1

                if constructor_button.is_pressed(event.pos):
                    scene = 5

            if scene == 3:
                if back_button_from_htp.is_pressed(event.pos):
                    scene = 0

            if scene == 2:
                if back_button_from_settings.is_pressed(event.pos):
                    scene = 0

            if scene == 1:
                if pause_btn.is_pressed(event.pos):
                    scene = 4

            if scene == 4:
                if start_button.is_pressed(event.pos):
                    scene = 1
                if exit_to_main.is_pressed(event.pos):
                    scene = 0
            if scene == 5:
                if save_map_button.is_pressed(event.pos):
                    save_map()
                
    if scene == 0:
        main_menu()
    elif scene == 1:
        start_pos()
        items.draw(window)   
        enemys.update(window)
        enemys.spawn()

        
        current_time = pg.time.get_ticks()
        if current_time - last_call_time > interval:
            last_call_time = current_time
            interval = randint(900, 2500) 

    elif scene == 2:
        setting()
    elif scene == 3:
        display_rules(window)
    elif scene == 4:
        pause()
    elif scene == 5:
        map_constructor(window)
    

    if hero_lives == 0:
        lose()


    pg.display.update()
pg.quit()
