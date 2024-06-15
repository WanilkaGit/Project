import pygame as pg
from maxym import Button, TextureButton, CheckButton, Bullet, Enemy, EnemySpawner, CheckButtonGroup
from ivan import items
pg.init()

font = pg.font.Font(None, 32)
pg.font.init()
score = 0
time_delay = 2
hero_lives = 3
### об'єкти кнопок ###
                    ###  кнопки, що в головному меню  ###
how_to_play_btn = Button(630, 200, 200, 80, font, 'How to play', (100, 10, 10))
play_btn = Button(630, 300, 200, 80, font, 'Play', (100, 10, 10))
setting_btn = Button(630, 400, 200, 80, font, 'Settings', (100, 10, 10))
exit_btn = Button(630, 500, 200, 80, font, 'Exit', (100, 10, 10))
constructor_button = Button(630, 700, 200, 80, font, 'Constructor', (100, 10, 10))

back_button_from_settings = TextureButton(630, 600, 100, 100, "assets\\textures\\ui\\back.png", font)
                    ###  кнопки, що в меню паузи  ###
start_button = TextureButton(630, 400, 100, 80, "assets\\textures\\ui\\play.png", font)
exit_to_main = TextureButton(430, 400, 100, 80, "assets\\textures\\ui\\home.png", font)
restart_btn = TextureButton(830, 400, 100, 80, "assets\\textures\\ui\\restart.png", font)
                    ###  група кнопок в меню налаштувань   ###
btn1 = CheckButton(50, 250, 50, font, 'Легкий')
btn2 = CheckButton(300, 250, 50, font, 'Середній')
btn3 = CheckButton(650, 250, 50, font, 'Важкий')

enemy = pg.transform.scale(pg.image.load("assets\\textures\\player\\tank1.png"), (70, 70))
bullet = pg.transform.scale(pg.image.load("assets\\textures\\blocks\\bullet.png"), (30, 10))
bullet_obj = Bullet(bullet, 3, damage = 1)
enemy_tank1 = Enemy(enemy, 1 , 100, 120, 0, 0, bullet_obj, items)
enemys = EnemySpawner([enemy_tank1, enemy_tank1], ((650,250),(650,250)))


restart_txt = font.render('Restart', True, (255, 0, 255))

class Jump_text(pg.sprite.Sprite):          #клас для з'являня тексту зліва на право з затримкою
    def __init__(self, x, y, width, height, speed, image):    #конструктор класу
        super().__init__()
        self. width = width
        self. height = height
        self. speed = speed
        self.image = restart_txt
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def reset(self, window):    #функція для відображення персонажів
        window.blit(self.image, (self.rect.x, self.rect.y))

    def plays(self):
        self.rect.x += self.speed

    def stop(self):
        pg.time.delay(7)

    
restart_text = Jump_text(100, 300, 50, 50, time_delay, restart_txt)

def main_menu(window):        #головне меню гри
        # відмальовка об'єктів #
    how_to_play_btn.draw(window)
    play_btn.draw(window)
    setting_btn.draw(window)
    exit_btn.draw(window)
    constructor_button.draw(window)

def setting(window):      #меню налаштувань
    window.fill((135, 95, 22))
    title = font.render('Налаштування', True, (0,0,0))
    title2 = font.render('Складність гри', True, (0,0,0))

    btn = CheckButtonGroup(btn1, btn2, btn3)
    back_button_from_settings.draw(window)
    btn.update(window)
    window.blit(title, (500, 30))
    window.blit(title2, (100, 100))

def pause(window):            #меню паузи
    window.fill((135, 95, 22))
    title = font.render('---Pause---', True, (0,0,0))
    title2 = font.render('Рахунок: '+ str(score), True, (0,0,0))
    title3 = font.render('Життя: '+  str(hero_lives), True, (0,0,0))
    window.blit(title,(500, 100))
    window.blit(title2,(300, 150))
    window.blit(title3,(300, 250))
    start_button.draw(window)
    exit_to_main.draw(window)
    restart_btn.draw(window)
    
def restart():      #рестарт гри
    global score, scene, hero_lives
    score = 0
    hero_lives = 3
    scene = 6


