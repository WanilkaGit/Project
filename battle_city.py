import pygame as pg
from oleksii import *
from maxym import *
from sonya import *
from ivan import *
from kostya import *
import ivan

pg.init()
pg.font.init()
pg.mixer.init()

BLACK = [0, 0, 0]
is_it_is = True

window = pg.display.set_mode((0, 0), pg.FULLSCREEN)
W, H = pg.display.Info().current_w, pg.display.Info().current_h

pg.display.set_caption('Battle City')
pg.display.set_icon(pg.image.load('assets\\textures\\fon1.jpg'))  #завантажуєемо фото іконки
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
                    restart()
                    restart_text.reset(window)
                    restart_text.plays()
                    if restart_text.rect.x >= 550 and restart_text.rect.x <= 1000:
                        restart_text.stop()
                    

            if scene == 5:          #якщо редактор карт
                if save_map_button.is_pressed(event.pos):
                    save_map()
                elif load_map_button.is_pressed(event.pos):
                    load_constructor_map()
                elif main_menu_button.is_pressed(event.pos):
                    map_constructor_uninit()
                    scene = 0

            if scene == 6:      #якщо рестарт гри
                if restart_btn.is_pressed(event.pos):
                    restart()
                    restart_text.reset(window)
                    restart_text.plays()
                    if restart_text.rect.x >= 550 and restart_text.rect.x <= 1000:
                        restart_text.stop()
                
    if scene == 0:
        main_menu(window)
    elif scene == 1:
        window.fill((135, 95, 22))
        window.blit(score_txt, (1100, 40))
        pause_btn.draw(window)
        window.blit(life_txt, (700, 10))
        if is_it_is:
            start_pos(map_lvl1)
            enemys.spawns = ivan.enemy_coordinates
            is_it_is = False
        players.draw(window)
        players.update()
        items.draw(window)
        enemys.update(window)

        
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
        
        

    if hero_lives == 0:
        lose(window)

    fps = font.render(f'FPS: {str(round(clock.get_fps()))}',True, (255,0,0))
    window.blit(fps, (10, 10))
    clock.tick(60)
    pg.display.update()
pg.quit()