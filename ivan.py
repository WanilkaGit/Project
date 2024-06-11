"""------------------------------------Імпорта----------------------------------------"""
import time

from pygame import*# імпорт пайгейма
print()
init()# ініціалізуєм пайгейм

"""------------------------------------Map build--------------------------------------"""
map_lvl1 = {
    "_________________",#Unbreakeble - u
    "|gggggggggggggggg|",#breakeable - b
    "|gb bbbb  bbbb bg|",#green_hide - g
    "|gb b  b  b  b bg|",#dark_white_hide - d
    "|gb bbbb  b  b bg|",#enemy - e
    "|gb    b  b  b bg|",#player1 - p
    "|gb bbbb  bbbb bg|",#lose - l
    "|gb  bb    bb  bg|",#win - w
    "|gb  bb bb bb  bg|",#кожен елемент цього
    "|gb    bbbb    bg|",#є частиню карти окрім
    "|gggggggggggggggg|",#пробілів
    "|u     b b      u|",#що вони означають написано вище
    "|g  b  bbb   b bg|",#теж зі знаком коментаря
    "|gb b  b b   b bg|",
    "|gb bu      ub bg|",
    "|gb b  bbb   b bg|",
    "|ggg   blb    gg |",
    "__________________"
    }

"""----------------Картинки щоб швидше вставляти бо по іншому довго-------------------"""
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


font1 = font.SysFont("Arial", 35)
font2 = font.SysFont(('font/ariblk.ttf'), 60)

texture_size = 40
# це те скільки вийде блоків на екрані 40 кількість пікселів на оин силвол
level1_width = len(map_lvl1[0]) * texture_size
level1_height = len(map_lvl1) * texture_size

#розміри екрану
W = 1280
H = 720

# створюєм вікно
window = display.set_mode((W, H))

"""-------------------------------------Класи---------------------------------------"""
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


"""----------------------------------ФУНКЦІЇ------------------------------------------"""
x = 0
y = 0
def start_pos():# стартова позиція
    global items, hero, unbreakables, breakables, green_hides, dark_white_hides, enemys, texture_size
    
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
            if c == "b":# дім полу
                b = Settings(x,y, texture_size, texture_size, 0, platform)# створюєм раба платформа
                breakables.append(b)
		items.add(b)
	    if c == "u":
		u = Settings(x, y, texture_size, texture_size, 0, platform)
		unbreakables.append(u)
		items.add(u)
	    if c == "g":
		g = Settings(x, y,texture_size, texture_size, 0, platform)
		green_hides.append(g)
		items.add(g)
	    if c == "d":
		d = Settings(x, y, texture_size, texture_size, 0, platform)
		dark_white_hides.append(d)
		items.add(d)
	    if c == "e":
		e = Settings(x, y, texture_size, texture_size, 0, platform)
		enemys.append(e)
		items.add(e)
	    if c == "p":
		hero = Player(300, 650, 50, 50 , 15, hero_l)
		items.add(hero)
	    if c == "l":
		l = Settings(x, y, texture_size, texture_size, 0, platform)
            x += texture_size#  ікси плюс 40
        y += texture_size#  перміщаємось в низ
        x = 0#  ікси 0

start_pos()# запускаєм дві функції
