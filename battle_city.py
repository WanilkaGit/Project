import pygame as pg
from oleksii import *
from maxym import *
from sonya import *
from ivan import *
from kostya import *
import ivan
import maxym

pg.init()
pg.font.init()
pg.mixer.init()

BLACK = [0, 0, 0]
is_it_is = True

window = pg.display.set_mode((0, 0), pg.FULLSCREEN)
W, H = pg.display.Info().current_w, pg.display.Info().current_h

pg.display.set_caption('Battle City')
pg.display.set_icon(pg.image.load('assets\\textures\\player\\player11.png'))  #завантажуєемо фото іконки
back = pg.transform.scale(pg.image.load('assets\\textures\\fon1.jpg'), (W, H))  #завантажуєемо картинку фона і розтягємо її у рзміри екрана
game = True

scene = 0

clock = pg.time.Clock()

last_call_time = pg.time.get_ticks()
interval = 100

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

                elif setting_btn.is_pressed(event.pos):
                    scene = 2

                elif how_to_play_btn.is_pressed(event.pos):
                    scene = 3

                elif play_btn.is_pressed(event.pos):
                    scene = 1

                if constructor_button.is_pressed(event.pos):
                    scene = 5

            if scene == 1:          #якщо меню гри
                if pause_btn.is_pressed(event.pos):
                    scene = 4

            elif scene == 2:          #якщо налаштування
                if back_button_from_settings.is_pressed(event.pos):
                    scene = 0

            elif scene == 3:          #якщо правила гри
                if back_button_from_htp.is_pressed(event.pos):
                    scene = 0

            elif scene == 4:              #якщо пауза
                if start_button.is_pressed(event.pos):
                    scene = 1
                elif exit_to_main.is_pressed(event.pos):
                    scene = 0
                if restart_btn.is_pressed(event.pos):
                    scene = 6
                    

            elif scene == 5:          #якщо редактор карт
                if save_map_button.is_pressed(event.pos):
                    scene = 7
                elif load_map_button.is_pressed(event.pos):
                    scene = 8
                elif play_constructor_button.is_pressed(event.pos):
                    create_map(map_to_list(constructor_blocks), 46)
                    scene = 9
                elif reset_button.is_pressed(event.pos):
                    maxym.constructor_blocks = pg.sprite.Group()
                elif main_menu_button.is_pressed(event.pos):
                    map_constructor_uninit()
                    scene = 0
                

            elif scene == 7:
                if save_slot1.is_pressed(event.pos):
                    save_map('save_slot1')
                    scene = 5
                elif save_slot2.is_pressed(event.pos):
                    save_map('save_slot2')
                    scene = 5
                elif save_slot3.is_pressed(event.pos):
                    save_map('save_slot3')
                    scene = 5
                elif save_slot4.is_pressed(event.pos):
                    save_map('save_slot4')
                    scene = 5
            
            elif scene == 8:
                if load_slot1.is_pressed(event.pos):
                    load_constructor_map('save_slot1')
                    scene = 5
                elif load_slot2.is_pressed(event.pos):
                    load_constructor_map('save_slot2')
                    scene = 5
                elif load_slot3.is_pressed(event.pos):
                    load_constructor_map('save_slot3')
                    scene = 5
                elif load_slot4.is_pressed(event.pos):
                    load_constructor_map('save_slot4')
                    scene = 5

    if scene == 0:
        main_menu(window)
    elif scene == 1:
        games(window)
        if is_it_is:
            create_map(map_lvl1, tile_size)
            enemys.spawns = ivan.enemy_coordinates
            is_it_is = False
        
        current_time = pg.time.get_ticks()
        if current_time - last_call_time > interval:
            last_call_time = current_time
            enemys.spawn()
            interval = randint(100, 2500)

    elif scene == 2:
        setting(window)

    elif scene == 3:
        display_rules(window)

    elif scene == 4:
        pause(window)
    
    elif scene == 5:
        map_constructor(window)
    
    elif scene == 6:
        restart()
        scene = 1
        restart_text.reset(window)
        
        if restart_text.rect.x >= 300 and restart_text.rect.x <= 900:
            restart_text.stop()
        restart_text.plays()

    elif scene == 7:
        save_map_scene(window)
    elif scene == 8:
        load_map_scene(window)

    elif scene == 9:
        constructor_play(window)
        

    if hero_lives == 0:
        lose(window)

    fps = font.render(f'FPS: {str(round(clock.get_fps()))}',True, (255,0,0))
    window.blit(fps, (10, 10))
    clock.tick(30)
    pg.display.update()
pg.quit()