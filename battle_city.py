import pygame as pg
from oleksii import *
from maxym import *
from sonya import *
from ivan import *
from kostya import *

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

                if setting_btn.is_pressed(event.pos):
                    scene = 2

                if how_to_play_btn.is_pressed(event.pos):
                    scene = 3

                if play_btn.is_pressed(event.pos):
                    scene = 1

                if constructor_button.is_pressed(event.pos):
                    scene = 5

            if scene == 3:          #якщо правила гри
                if back_button_from_htp.is_pressed(event.pos):
                    scene = 0

            if scene == 2:          #якщо налаштування
                if back_button_from_settings.is_pressed(event.pos):
                    scene = 0

            if scene == 1:          #якщо меню гри
                if pause_btn.is_pressed(event.pos):
                    scene = 4

            if scene == 4:              #якщо пауза
                if start_button.is_pressed(event.pos):
                    scene = 1
                if exit_to_main.is_pressed(event.pos):
                    scene = 0
                if restart_btn.is_pressed(event.pos):
                    restart(window)
                    scene = 1
                    restart_text.reset()
                    restart_text.plays()
                    if restart_text.rect.x >= 550 and restart_text.rect.x <= 1000:
                        restart_text.stop()
                    

            if scene == 5:          #якщо редактор карт
                if save_map_button.is_pressed(event.pos):
                    save_map()

            if scene == 6:      #якщо рестарт гри
                if restart_btn.is_pressed(event.pos):
                    restart(window)
                    restart_text.reset()
                    restart_text.plays()
                    if restart_text.rect.x >= 550 and restart_text.rect.x <= 1000:
                        restart_text.stop()
                
    if scene == 0:
        main_menu(window)
    elif scene == 1:
        window.fill((135, 95, 22))
        pause_btn.draw(window)
        window.blit(text_life, (700, 10))
        if is_it_is:
            start_pos(map_lvl1)
            is_it_is = False
        # window.fill((0,0,0))
        items.draw(window)
        enemys.update(window)
        enemys.spawn()

        
        current_time = pg.time.get_ticks()
        if current_time - last_call_time > interval:
            last_call_time = current_time
            interval = randint(100, 500) 

    elif scene == 2:
        setting(window)
    elif scene == 3:
        display_rules(window)
    elif scene == 4:
        pause(window)
        
    elif scene == 5:
        map_constructor(window)
    

    if hero_lives == 0:
        lose(window)

    fps = font.render(f'FPS: {str(round(clock.get_fps()))}',True, (255,0,0))
    window.blit(fps, (900, 700))
    clock.tick(60)
    pg.display.update()
pg.quit()



