from pygame import *

"""Map build"""
map_lvl1 = {
    "_________________",#Unbreakeble - u
    "|gggggggggggggggg/",#breakeable - b
    "|gb bbbb  bbbb bg/",#green_hide - g
    "|gb b  b  b  b bg/",#dark_white_hide - d
    "|gb bbbb  b  b bg/",#enemy - e
    "|gb    b  b  b bg/",#player1 - p
    "|gb bbbb  bbbb bg/",#lose - l
    "|gb  bb    bb  bg/",#win - w
    "|gb  bb bb bb  bg/",#кожен елемент цього
    "|gb    bbbb    bg/",#є частиню карти окрім
    "|gggggggggggggggg/",#пробілів
    "|u     b b      u/",#що вони означають написано вище
    "|g  b  bbb   b bg/",#теж зі знаком коментаря
    "|gb b  b b   b bg/",
    "|gb bu      ub bg/",
    "|gb b  bbb   b bg/",
    "|ggg   blb    gg /",
    "------------------"
}

"""Картинки щоб швидше вставляти бо по іншому довго"""

hero_r = "images/hero_r.png"
hero_l = "images/hero_l.png"

enemy_l = "images/enemy_l.png"
enemy_r = "images/enemy_r.png"

coin_img = "images/coin.png"
door_img = "images/door.png"
key_img = "images/key.png"
chest_open = "images/cst_open.png"
chest_close = "images/cst_close.png"
stairs = "images/stair.png"
portal_img = "images/portal.png"
platform = "images/platform.png"
power = "images/mana.png"
nothing = "images/nothing.png"
boss = "images/nothing.png"



h_m_c = 0
font1 = font.SysFont("Arial", 35)
font2 = font.SysFont(('font/ariblk.ttf'), 60)
e_tap = font2.render('press (e)', True, (255, 0, 255))
k_need = font2.render('You need a key to open!', True, (255, 0, 255))
space = font2.render('press (space) to kill the enemy', True, (255, 0, 255))

# це те скільки вийде блоків на екрані 40 кількість пікселів на оин силвол
level1_width = len(level1[0]) * 40
level1_height = len(level1) * 40

#розміри екрану
W = 1280
H = 720



# створюєм вікно
window = display.set_mode((W, H))


# Все для вікна
back = transform.scale(image.load("images/bgr.png"), (W, H))# фон
display.set_caption("Лошок")# назва
display.set_icon(image.load("images/key.png"))# картинка біля назви



"""Класи"""
class Settings(sprite.Sprite):# основний клас тут основні параметри
    def __init__(self, x, y, width, height, speed, img):
        super().__init__()
        self.width = width
        self.height = height
        self.speed = speed
        self.image = tansform.scale(image.load(img), (self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y



    def reset(self):# тут прописана функція ресет
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(Settings):# клас гравця з супер класом сетінгс
    def r_l(elf):# тут буде переміщення в право ліво
        global mana
        key_pressed = key.get_pressed()# задаєм в зміну значення
        if key_pressed[K_a]:# перевіряєм чи нажата кнопка це а
            self.rect.x -= self.speed# якщо так той демо в ліво
            self.image = transform.scale(image.load(hero_l), (self.width, self.height))# підсьтавляєм фотку
            kana.side = "left"

        if key_pressed[K_d]:#кнопка в низ натиснута
            self.rect.x += self.speed# х додаєм швидкість рухаємось
            self.image = transform.scale(image.load(hero_r), (self.width, self.height))#  підставляєм фотку
            mana.side = "right
            
        if key_pressed[K_s]:# якщо в низ тобто в низ
            self.rect.y += self.speed# ми додає тобто спускаємось

        if key_pressed[K_w]:# якщо в верх то віднімаєм піднімаємось
            self.rect.y -= self.speed# 

