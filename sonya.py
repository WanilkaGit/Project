import pygame as pg
from maxym import Button, TextureButton, CheckButton, Bullet, Enemy, EnemySpawner, CheckButtonGroup
from ivan import blocks, hides_blocks, font2, players
from random import choice, randint
import ivan as i
pg.init()


pg.font.init()

font_path = r"assets/textures/fonts/Blazma-Regular.otf"
font_size = 36
font = pg.font.Font(font_path, font_size)

#window = pg.display.set_mode((0, 0), pg.FULLSCREEN)
#W, H = pg.display.Info().current_w, pg.display.Info().current_h
#background_image = pg.image.load(r'assets/textures/background.jpg')
#background_image = pg.transform.scale(background_image, (W, H))

score = 0
score_txt = font.render("Score: "+str(score), True, (0,0,0))

time_delay = 2
hero_lives = 3
life_txt = font.render('Life: ' + str(hero_lives), True, (0,0,0))

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
btn3 = CheckButton(500, 250, 50, font, 'Важкий', text_color=(255, 255, 255))

enemy = pg.transform.scale(pg.image.load("assets/textures/enemys/enemytankdefult1.png"), (34, 34))
bullet = pg.transform.scale(pg.image.load("assets/textures/blocks/bullet.png"), (10, 10))
bullet_obj = Bullet(bullet, 3, damage = 1)
enemy_tank1 = Enemy(enemy, 1 , 100, 120, 0, 0, bullet_obj, blocks)
enemys = EnemySpawner([enemy_tank1, enemy_tank1, enemy_tank1, enemy_tank1, enemy_tank1])

restart_txt = font.render('Restart', True, (255, 0, 255))

            ### for pause menu  ###
window = pg.display.set_mode((0, 0), pg.FULLSCREEN)
W, H = pg.display.Info().current_w, pg.display.Info().current_h
background_image = pg.image.load(r'assets/textures/background.jpg')
background_image = pg.transform.scale(background_image, (W, H))

coin_img = pg.image.load("assets/textures/ui/coin.png")

class Jump_text(pg.sprite.Sprite):          #клас для з'являня тексту зліва на право з затримкою
    def __init__(self, x, y, width, height, speed, image):    #конструктор класу
        super().__init__()
        self. width = width
        self. height = height
        self. speed = speed
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def reset(self, window):    #функція для відображення персонажів
        window.blit(self.image, (self.rect.x, self.rect.y))

    def plays(self):
        self.rect.x += self.speed

    def stop(self):
        self.speed = 4

    
restart_text = Jump_text(100, 300, 50, 50, 10, restart_txt)

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

    btn = CheckButtonGroup(btn1, btn2, btn3)
    back_button_from_settings.draw(window)
    btn.update(window)
    window.blit(title, (650, 30))
    window.blit(title2, (90, 100))

def pause(window):            #меню паузи
    #window.fill((135, 95, 22))
    window.blit(background_image, (0,0))
    title = font.render('---Pause---', True, (255, 255, 255))
    title2 = font.render('Рахунок: '+ str(score), True, (255, 255, 255))
    title3 = font.render('Життя: '+  str(hero_lives), True, (255, 255, 255))
    window.blit(title,(500, 100))
    window.blit(title2,(300, 150))
    window.blit(title3,(300, 250))
    start_button.draw(window)
    exit_to_main.draw(window)
    restart_btn.draw(window)
    
def restart():      #рестарт гри
    global score, hero_lives
    score = 0
    hero_lives = 3

def games(window):
    window.fill((93, 62, 10))
    window.blit(score_txt, (1000, 10))
    pause_btn.draw(window)
    window.blit(life_txt, (1000, 60))
    players.draw(window)
    players.update()
    enemys.update(window)
    blocks.draw(window)
    hides_blocks.draw(window)

start_time = pg.time.get_ticks()



class Buster:
    def __init__(self, image, interval, action):
        self.image = image
        self.interval = interval
        self.action = action

        last_call_time = pg.time.get_ticks()

    def buster_spawn(self):
        p = choice((i.empty_coordinates))
        window.blit(self.image, p)
    
    def time_delay(self, window):
        if self.image not in window:
            if start_time - last_call_time > interval:
                last_call_time = start_time
                coin.buster_spawn()
                interval = randint(100, 500) 
                
def add_point():
    pass

coin = Buster(coin_img, 10, add_point())




    




