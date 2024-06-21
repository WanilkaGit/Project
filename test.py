import pygame as pg
from oleksii import *
from maxym import *
from sonya import *
from ivan import *
from kostya import *

# pg.init()
# pg.font.init()
# pg.mixer.init()

# BLACK = [0, 0, 0]
# is_it_is = True

# window = pg.display.set_mode((0, 0), pg.FULLSCREEN)
# W, H = pg.display.Info().current_w, pg.display.Info().current_h

# pg.display.set_caption('Battle City')
# pg.display.set_icon(pg.image.load('assets\\textures\\fon1.jpg'))  #завантажуєемо фото іконки
# back = pg.transform.scale(pg.image.load('assets\\textures\\fon1.jpg'), (W, H))  #завантажуєемо картинку фона і розтягємо її у рзміри екрана
# game = True


# scene = 0

# last_call_time = pg.time.get_ticks()
# interval = 100

# while game:
#     window.blit(back, (0,0))
#     for event in pg.event.get():
#         if event.type == pg.QUIT:
#             game = False
#         if event.type == pg.KEYDOWN:
#             if event.key == pg.K_ESCAPE:
#                 game = False         
#         if event.type == pg.MOUSEBUTTONDOWN:
#             if scene == 0:
#                 if exit_btn.is_pressed(event.pos):
#                     game = False 

#                 if setting_btn.is_pressed(event.pos):
#                     scene = 2

#                 if how_to_play_btn.is_pressed(event.pos):
#                     scene = 3

#                 if play_btn.is_pressed(event.pos):
#                     scene = 1

#                 if constructor_button.is_pressed(event.pos):
#                     scene = 5

#             if scene == 3:
#                 if back_button_from_htp.is_pressed(event.pos):
#                     scene = 0

#             if scene == 2:
#                 if back_button_from_settings.is_pressed(event.pos):
#                     scene = 0

#             if scene == 1:
#                 if pause_btn.is_pressed(event.pos):
#                     scene = 4

#             if scene == 4:
#                 if start_button.is_pressed(event.pos):
#                     scene = 1
#                 if exit_to_main.is_pressed(event.pos):
#                     scene = 0
#             if scene == 5:
#                 if save_map_button.is_pressed(event.pos):
#                     save_map()

#             #if scene == 6:
#                 #if restart_btn.is_pressed(event.pos):
#                 # restart()
#                 #  restart_text.reset()
#                 #  restart_text.plays()
#                 #  if restart_text.rect.x >= 550 and restart_text.rect.x <= 1000:
#                 #     restart_text.stop()
                
#     if scene == 0:
#         main_menu()
#     elif scene == 1:
#         if is_it_is:
#             start_pos(map_lvl1)
#             is_it_is = False
#         # window.fill((0,0,0))
#         items.draw(window)
#         # enemys.update(window)
#         # enemys.spawn()

        
#         current_time = pg.time.get_ticks()
#         if current_time - last_call_time > interval:
#             last_call_time = current_time
#             interval = randint(100, 500) 

#     elif scene == 2:
#         setting()
#     elif scene == 3:
#         display_rules(window)
#     elif scene == 4:
#         pause()
        
#     elif scene == 5:
#         map_constructor(window)
    

#     if hero_lives == 0:
#         lose()
#         scene = 6


#     pg.display.update()
# pg.quit()

def create_map(map: list | str | tuple, tile_size: int, begin_x: int = 0, begin_y: int = 70):# стартова позиція
    global blocks, hides_blocks, players, unbreakables, breakables, green_hides, dark_white_hides, enemy_coordinates, empty_coordinates

    breakables = list()
    unbreakables = list()
    green_hides = list()
    dark_white_hides = list()
    enemy_coordinates = list()
    empty_coordinates = list()

    # всі списки дивіться в кінотеатрах(коді)
    x = begin_x#  координати для обєктів
    y = begin_y
    for r in map:# фор як раб почав ходити по списками перевіряєм індекси
        for c in r:#  стучим в двері перевіряєм чи
            if c == " ":
                empty_coordinates = creating_lists_coordinate(empty_coordinates, x, y)
            if c == "b":# дім полу
                b = Blocks(x,y, tile_size, tile_size, 0, breakable, True, False)# створюєм раба платформа
                breakables.append(b)
                blocks.add(b)
            if c == "u":
                u = Blocks(x, y, tile_size, tile_size, 0, unbreakable, False, False)
                unbreakables.append(u)
                blocks.add(u)
            if c == "g":
                g = Blocks(x, y,tile_size, tile_size, 0, green_hide, False, True)
                green_hides.append(g)
                hides_blocks.add(g)
            if c == "d":
                d = Blocks(x, y, tile_size, tile_size, 0, green_hide, False, True)
                dark_white_hides.append(d)
                blocks.add(d)
            if c == "e":
                enemy_coordinates = creating_lists_coordinate(enemy_coordinates, x, y)
            if c == "p":
                hero = Player(x, y, 34, 34 , 1, player1, True, False)
                players.add(hero)
            if c == "l":
                l = Blocks(x, y, tile_size, tile_size, 0, breakable, False, False)
            if c == "|":
                p = Blocks(x, y, tile_size, tile_size, 0, breakable, False, False)
                blocks.add(p)
            x += tile_size#  ікси плюс tile_size
        y += tile_size#  перміщаємось в низ на tile_size
        x = begin_x#  ікси begin_x