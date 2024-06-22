import pygame as pg
from oleksii import *
from maxym import *
from sonya import *
from ivan import *
from kostya import *
import ivan
import json
import time
from threading import Timer

pg.init()
pg.font.init()
pg.mixer.init()

BLACK = [0, 0, 0]
is_it_is = True

window = pg.display.set_mode((0, 0), pg.FULLSCREEN)
W, H = pg.display.Info().current_w, pg.display.Info().current_h

pg.display.set_caption('Battle City')
pg.display.set_icon(pg.image.load('assets/textures/player/player11.png'))  #завантажуєемо фото іконки
back = pg.transform.scale(pg.image.load('assets/textures/fon1.jpg'), (W, H))  #завантажуєемо картинку фона і розтягємо її у рзміри екрана
game = True

scene = 0

clock = pg.time.Clock()

last_call_time = pg.time.get_ticks()
interval = 100

incrementing = True
score = 0


# def increment_score():
#     global score, incrementing
#     if incrementing:
#         score += 1
#         save_to_file({'score': score}, filename)
#         print(f'Score: {score}')
#         Timer(1, increment_score).start()

def start_increment():
    global incrementing
    if not incrementing:
        incrementing = True
        # increment_score()

def stop_increment():
    global incrementing
    incrementing = False


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
                stop_increment()
                if exit_btn.is_pressed(event.pos):
                    game = False 

                elif setting_btn.is_pressed(event.pos):
                    scene = 2

                elif how_to_play_btn.is_pressed(event.pos):
                    scene = 3

                elif play_btn.is_pressed(event.pos):
                    create_map(map_lvl1, tile_size, beginers[0], beginers[1])
                    enemys.spawns = ivan.enemy_coordinates
                    scene = 1

                if constructor_button.is_pressed(event.pos):
                    scene = 5

            if scene == 1:
                filename = 'score.json'

                def save_to_file(data, filename):
                    with open(filename, 'w') as file:
                        json.dump(data, file)
                # реалізаці вигрузки даних з файлу
                # try:
                #     with open(filename, 'r') as file:
                #         data = json.load(file)
                #         score = data.get('score', 0)
                # except FileNotFoundError:
                #     pass
                start_increment()
                        #якщо меню гри
                if pause_btn.is_pressed(event.pos):
                    scene = 4

            elif scene == 2:
                stop_increment()          #якщо налаштування
                if back_button_from_settings.is_pressed(event.pos):
                    scene = 0

            elif scene == 3:
                stop_increment()          #якщо правила гри
                if back_button_from_htp.is_pressed(event.pos):
                    scene = 0

            elif scene == 4:
                stop_increment()              #якщо пауза
                if start_button.is_pressed(event.pos):
                    scene = 1
                elif exit_to_main.is_pressed(event.pos):
                    reset_map()
                    enemys.reset_enemys()
                    scene = 0
                elif restart_btn.is_pressed(event.pos):
                    reset_map()
                    create_map(map_lvl1, tile_size)
                    enemys.reset_enemys()
                    scene = 6

            elif scene == 5:
                stop_increment()  # Якщо сцена - редактор карт
                if maxyms_scenes.save_map_button.is_pressed(event.pos) and maxyms_scenes.check_provisos():
                    maxyms_scenes.load_slots_names()
                    scene = 7
                elif maxyms_scenes.load_map_button.is_pressed(event.pos):
                    maxyms_scenes.load_slots_names()
                    scene = 8 
                elif maxyms_scenes.play_constructor_button.is_pressed(event.pos) and maxyms_scenes.check_provisos():
                    maxyms_scenes.last_call_time = pg.time.get_ticks()
                    maxyms_scenes.interval = 250
                    maxyms_scenes.game_blocks, maxyms_scenes.hides_blocks, maxyms_scenes.players, maxyms_scenes.spawner.spawns = create_map(maxyms_scenes.map_to_list(maxyms_scenes.constructor_blocks), (32,32))
                    maxyms_scenes.spawner.change_enemy_list([enemy_defuld, enemy_defuld, enemy_defuld, enemy_defuld, enemy_defuld, enemy_defuld, enemy_speed, enemy_speed, enemy_speed, enemy_shield, enemy_shield, enemy_shield, enemy_agility, enemy_mono, enemy_rc])
                    scene = 9
                elif maxyms_scenes.reset_button.is_pressed(event.pos):
                    maxyms_scenes.constructor_blocks = pg.sprite.Group()
                elif maxyms_scenes.main_menu_button.is_pressed(event.pos):
                    maxyms_scenes.map_constructor_uninit()
                    scene = 0

            elif scene == 7:
                stop_increment()  # Якщо сцена - збереження карт
                if maxyms_scenes.save_slot1.is_pressed(event.pos):
                    maxyms_scenes.save_map('save_slot1')
                    scene = 5
                elif maxyms_scenes.save_slot2.is_pressed(event.pos):
                    maxyms_scenes.save_map('save_slot2')
                    scene = 5
                elif maxyms_scenes.save_slot3.is_pressed(event.pos):
                    maxyms_scenes.save_map('save_slot3')
                    scene = 5
                elif maxyms_scenes.save_slot4.is_pressed(event.pos):
                    maxyms_scenes.save_map('save_slot4')
                    scene = 5
                elif maxyms_scenes.back_to_constructor_button.is_pressed(event.pos):
                    scene = 5

            elif scene == 8:
                stop_increment()  # Якщо сцена - завантаження карт
                if maxyms_scenes.load_slot1.is_pressed(event.pos):
                    maxyms_scenes.load_constructor_map('save_slot1')
                    scene = 5
                elif maxyms_scenes.load_slot2.is_pressed(event.pos):
                    maxyms_scenes.load_constructor_map('save_slot2')
                    scene = 5
                elif maxyms_scenes.load_slot3.is_pressed(event.pos):
                    maxyms_scenes.load_constructor_map('save_slot3')
                    scene = 5
                elif maxyms_scenes.load_slot4.is_pressed(event.pos):
                    maxyms_scenes.load_constructor_map('save_slot4')
                    scene = 5
                elif maxyms_scenes.back_to_constructor_button.is_pressed(event.pos):
                    scene = 5
            elif scene == 9: # якщо сцена гри в зроблену власноруч карту
                if maxyms_scenes.back_to_constructor_from_test_button.is_pressed(event.pos):
                    reset_map()
                    maxyms_scenes.spawner.reset_enemys()
                    scene = 5
        if scene == 5:
            maxyms_scenes.map_name_line.update(event)

    if scene == 0:
        main_menu(window)
    elif scene == 1:
        games(window)
        if is_it_is:
            # create_map(map_lvl1, tile_size)
            # enemys.spawns = ivan.enemy_coordinates
            is_it_is = False
        
        current_time = pg.time.get_ticks()
        if current_time - last_call_time > interval:
            last_call_time = current_time
            enemys.spawn_random()
            interval = randint(500, 3500)

    elif scene == 2:
        setting(window)

    elif scene == 3:
        display_rules(window)

    elif scene == 4:
        pause(window)
    
    elif scene == 5:
        maxyms_scenes.map_constructor(window)
    
    elif scene == 6:
        restart()
        scene = 1
        restart_text.reset(window)
        
        if restart_text.rect.x >= 300 and restart_text.rect.x <= 900:
            restart_text.stop()
        restart_text.plays()

    elif scene == 7:
        maxyms_scenes.save_map_scene(window)
    elif scene == 8:
        maxyms_scenes.load_map_scene(window)

    elif scene == 9:
        maxyms_scenes.constructor_play(window)
        

    if hero_lives == 0:
        lose(window)

    fps = font.render(f'FPS: {str(round(clock.get_fps()))}',True, (255,0,0))
    window.blit(fps, (10, 10))
    clock.tick(30)
    pg.display.update()
pg.quit()