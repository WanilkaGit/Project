import pygame as pg
from maxym import Button, TextureButton, CheckButton, Bullet, Enemy, EnemySpawner, CheckButtonGroup
from ivan import blocks, hides_blocks, font2, players, bullets, level1_width, level1_height, beginers, loozes, score
import ivan as i
pg.init()


pg.font.init()

font_path = r"assets/textures/fonts/Blazma-Regular.otf"
font_size = 36
font = pg.font.Font(font_path, font_size)

time_delay = 2


pause_btn = TextureButton(1300, 20, 50, 50, "assets/textures/ui/pause.png", font2)

### об'єкти кнопок ###
                    ###  кнопки, що в головному меню  ###
play_btn = Button(630, 200, 260, 100, font, 'Play', (100, 10, 10))
how_to_play_btn = Button(630, 300, 260, 100, font, 'How to play', (100, 10, 10))
setting_btn = Button(630, 400, 260, 100, font, 'Settings', (100, 10, 10))
constructor_button = Button(630, 500, 260, 100, font, 'Constructor', (100, 10, 10))
exit_btn = Button(630, 700, 260, 100, font, 'Exit', (100, 10, 10))

back_button_from_settings = TextureButton(20, 760, 230, 100, "assets/textures/ui/back2.png", font)
                    ###  кнопки, що в меню паузи  ###
start_button = TextureButton(630, 400, 100, 80, "assets/textures/ui/play.png", font)
exit_to_main = TextureButton(430, 400, 100, 80, "assets/textures/ui/home.png", font)
restart_btn = TextureButton(830, 400, 100, 80, "assets/textures/ui/restart.png", font)
                    ###  група кнопок в меню налаштувань   ###
btn1 = CheckButton(100, 250, 50, font, 'Легкий', text_color=(255, 255, 255))
btn2 = CheckButton(300, 250, 50, font, 'Середній', text_color=(255, 255, 255))
btn2.button_pressed = True
btn3 = CheckButton(500, 250, 50, font, 'Важкий', text_color=(255, 255, 255))

dificlty = CheckButtonGroup(btn1, btn2, btn3)

fps_text = font.render('показувати фпс', True, (255, 255, 255))
fps_on = CheckButton(200, 600, 50, font, 'так', text_color=(255, 255, 255))
fps_off = CheckButton(300, 600, 50, font, 'ні', text_color=(255, 255, 255))
fps_off.button_pressed = True

fps_chg = CheckButtonGroup(fps_on, fps_off)

coop_text = font.render('додати другого гравця', True, (255, 255, 255))
add_coop = CheckButton(200, 450, 50, font, 'так', text_color=(255, 255, 255))
not_add_coop = CheckButton(300, 450, 50, font, 'ні', text_color=(255, 255, 255))
not_add_coop.button_pressed = True

coop_group = CheckButtonGroup(add_coop, not_add_coop)

enemy_defuld_sprite = (pg.transform.scale(pg.image.load("assets/textures/enemys/enemytankdefult1.png"), (28, 28)), 
                        pg.transform.scale(pg.image.load("assets/textures/enemys/enemytankdefult2.png"), (28, 28)))

enemy_speed_sprite = (pg.transform.scale(pg.image.load("assets/textures/enemys/enemytankspeed1.png"), (28, 28)), 
                        pg.transform.scale(pg.image.load("assets/textures/enemys/enemytankspeed2.png"), (28, 28)))

enemy_shield_sprite = (pg.transform.scale(pg.image.load("assets/textures/enemys/enemytankshield1.png"), (28, 28)),
                        pg.transform.scale(pg.image.load("assets/textures/enemys/enemytankshield2.png"), (28, 28)))

enemy_agility_sprite = (pg.transform.scale(pg.image.load("assets/textures/enemys/enemytankagility1.png"), (28, 28)),
                        pg.transform.scale(pg.image.load("assets/textures/enemys/enemytankagility2.png"), (28, 28)))

enemy_mono_sprite = (pg.transform.scale(pg.image.load("assets/textures/enemys/enemytankmono1.png"), (28, 28)),
                        pg.transform.scale(pg.image.load("assets/textures/enemys/enemytankmono2.png"), (28, 28)))

enemy_rc_sprite = (pg.transform.scale(pg.image.load("assets/textures/enemys/enemytankrc1.png"), (16, 16)),
                    pg.transform.scale(pg.image.load("assets/textures/enemys/enemytankrc2.png"), (16, 16)))

bullet = pg.transform.scale(pg.image.load("assets/textures/bullet.png"), (3, 5))
bullet_obj = Bullet(bullet, 3, damage = 1)

enemy_defuld = Enemy(enemy_defuld_sprite, 1 , 60, 120, 1, 100, bullet_obj, blocks, players, loozes)
enemy_speed = Enemy(enemy_speed_sprite, 2 , 45, 110, 1, 150, bullet_obj, blocks, players, loozes)
enemy_shield = Enemy(enemy_shield_sprite, 1 , 63, 125, 3, 150, bullet_obj, blocks, players, loozes)
enemy_agility = Enemy(enemy_agility_sprite, 1 , 7, 110, 1, 150, bullet_obj, blocks, players, loozes)
enemy_mono = Enemy(enemy_mono_sprite, 1 , 0, 100, 5, 200, bullet_obj, blocks, players, loozes)
enemy_rc = Enemy(enemy_rc_sprite, 3, 45, 0, 1, 150, bullet_obj, blocks, players, loozes)

restart_text = font.render('Restart', True, (255, 0, 255))

enemys = EnemySpawner([enemy_defuld, enemy_defuld, enemy_defuld, enemy_defuld, enemy_defuld, enemy_defuld, enemy_speed, enemy_speed, enemy_speed, enemy_shield, enemy_shield, enemy_shield, enemy_agility, enemy_mono, enemy_rc], zone = (beginers[0], beginers[1], level1_width, level1_height))

            ### for pause menu  ###
window = pg.display.set_mode((0, 0), pg.FULLSCREEN)
W, H = pg.display.Info().current_w, pg.display.Info().current_h
background_image = pg.image.load(r'assets/textures/background.jpg')
background_image = pg.transform.scale(background_image, (W, H))

def main_menu(window):        #головне меню гри
        # відмальовка об'єктів #
    how_to_play_btn.draw(window)
    play_btn.draw(window)
    setting_btn.draw(window)
    exit_btn.draw(window)
    constructor_button.draw(window)

def setting(window):      #меню налаштувань
    window.blit(background_image, (0, 0))
    title = font.render('Налаштування', True, (255,255,255))
    title2 = font.render('Виберіть складність гри:', True, (255, 255, 255))
    
    back_button_from_settings.draw(window)
    dificlty.update(window)
    coop_group.update(window)
    fps_chg.update(window)
    change_settings()
    window.blit(coop_text, (90, 400))
    window.blit(fps_text, (90, 550))
    window.blit(title, (650, 30))
    window.blit(title2, (90, 100))

def pause(window):            #меню паузи
    #window.fill((135, 95, 22))
    window.blit(background_image, (0,0))
    title = font.render('---Pause---', True, (255, 255, 255))
    title2 = font.render('Рахунок: '+ str(score), True, (255, 255, 255))
    window.blit(title,(500, 100))
    window.blit(title2,(300, 150))
    start_button.draw(window)
    exit_to_main.draw(window)
    restart_btn.draw(window)
    
def restart():      #рестарт гри
    global score, hero_lives
    score = 0
    hero_lives = 3

def games(window):
    score_txt = font.render('score: ' + str(score), True, (0, 0, 0))
    window.fill((93, 62, 10))
    window.blit(score_txt, (1100, 20))
    pause_btn.draw(window)
    players.draw(window)
    players.update(window, blocks, enemys.enemy_group)
    bullets.draw(window)
    enemys.update(window)
    blocks.draw(window)
    loozes.draw(window)
    hides_blocks.draw(window)


def change_settings():
    if btn1.button_pressed:
        i.player_lives = 3
    elif btn2.button_pressed:
        i.player_lives = 2
    elif btn3.button_pressed:
        i.player_lives = 1
    if add_coop.button_pressed:
        i.friend_is_on = True
    elif not_add_coop.button_pressed:
        i.friend_is_on = False
    