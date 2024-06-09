"""Імпорта"""
import time

from pygame import*# імпорт пайгейма

init()# ініціалізуєм пайгейм

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

"""Класи"""
class Settings(sprite.Sprite):# основний клас тут основні параметри
    def __init__(self, x, y, width, height, speed, img):
        super().__init__()
        self.width = width
        self.height = height
        self.speed = speed
        self.image = transform.scale(image.load(img), (self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def reset(self):# тут прописана функція ресет
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(Settings):# клас гравця з супер класом сетінгс
    def r_l(self):# тут буде переміщення в право ліво
        global mana
        key_pressed = key.get_pressed()# задаєм в зміну значення
        if key_pressed[K_a]:# перевіряєм чи нажата кнопка це а
            self.rect.x -= self.speed# якщо так той демо в ліво
            self.image = transform.scale(image.load(hero_l), (self.width, self.height))# підсьтавляєм фотку
            
        if key_pressed[K_d]:#кнопка в низ натиснута
            self.rect.x += self.speed# х додаєм швидкість рухаємось
            self.image = transform.scale(image.load(hero_r), (self.width, self.height))#  підставляєм фотку
            
        if key_pressed[K_s]:# якщо в низ тобто в низ
            self.rect.y += self.speed# ми додає тобто спускаємось
            
        if key_pressed[K_w]:# якщо в верх то віднімаєм піднімаємось
            self.rect.y -= self.speed# 

x = 0
y = 0
def start_pos():# стартова позиція
    global items, camera, hero, block_r, block_l, plat, coins, door, coin
    global stairs_lst, enemy_lst, p6, p11, p7, p8, open_d, open_ch, manas# робимо глобальними змінни
    hero = Player(300, 650, 50, 50 , 15, hero_l)
    
    items = sprite.Group()#  створюємо тусу
    
	breakables = list()
	unbreakables = list()
	green_hides = list()
	dark_white_hides = list()
	enemys = list()
    
    # всі списки дивіться в кінотеатрах(коді)
    x = 0#  координати для обєктів
    y = 0
    for r in level1:# фор як раб почав ходити по списками перевіряєм індекси
        for c in r:#  стучим в двері перевіряєм чи
            if c == "-":# дім полу
                p1 = Settings(x,y, 40, 40, 0, platform)# створюєм раба платформа
                plat.append(p1)# 
                items.add(p1)
            if c == "l":# дім "далі ходу нема"
                p2 = Settings(x,y, 40, 40, 0, nothing)#  повітря
                block_l.append(p2)# вони сидять на двух стулах список
      dd(p2)# туса/група
            if c == "r":#  дім "далі ходу тож нема"
                p3 = Settings(x,y, 40, 40, 0, nothing)#  повітря
                block_r.append(p3)#в ходять в спи
                items.add(p3)# в туси/групи
            if c == "°":# дім бабла
                p4 = Settings(x,y, 40, 40, 0, coin_img)#  бабла/грошей
                coins.append(p4)#в ходять в спи
                items.add(p4)# в туси/групи
            if c == "/":# дім рабів пояких мона ходить
                p5 = Settings(x, y - 40, 40, 180, 0, stairs)# сходів
                stairs_lst.append(p5)#в ходять в спи
                items.add(p5)# в туси/групи
            if c == "k":
                p6 = Settings(x,y + 20, 40, 20, 0, key_img)#  ключа
                items.add(p6)
            if c == "g":
                p7 = Settings(x,y + 20, 80, 60, 0, chest_close)#  ключа
                items.add(p7)
            if c == "d":
                door = Settings(x,y, 40, 80, 0, door_img)#  ключа
                items.add(door)
            if c  == "e":
                p9 = Enemy(x,y, 40, 40, 20, enemy_r, "right")
                enemy_lst.append(p9)
                items.add(p9)
            if c  == "m":
                p10 = Enemy(x,y, 40, 40, 20, enemy_l, "left")
                enemy_lst.append(p10)
                items.add(p10)
            if c == "c":
                p11 = Settings(x,y + 20, 40, 20, 0, key_img)#  ключа
                items.add(p11)
            x += 40#  ікси плюс 40
        y += 40#  перміщаємось в низ
        x = 0#  ікси 0
    items.add(hero)

start_pos()# запускаєм дві функції
lvl_1()
