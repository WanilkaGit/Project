"""------------------------------------Імпорта----------------------------------------"""
import time
from maxym import TextureButton
from random import choices, choice
from pygame import*# імпорт пайгейма
from oleksii import text_life
init()# ініціалізуєм пайгейм


"""------------------------------------Map build--------------------------------------"""
map_lvl1 = [
    "_________________",#Unbreakeble - u
    "|gggggggggggggggg|",#breakeable - b
    "|gb bbbb  bbbb bg|",#green_hide - g
    "|gb b  b  b  b bg|",#dark_white_hide - d
    "|gb bbbb  b  b bg|",#enemy - e
    "|gb    b  b  b bg|",#player1 - p
    "|gb bbbb  bbbb bg|",#lose - l
    "|gb            bg|",#win - w
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
]

items = sprite.Group()#  створюємо тусу
pl_items = sprite.Group()

"""----------------Картинки щоб швидше вставляти бо по іншому довго-------------------"""
player1 = "assets/textures/player/player11.png"
player1_moves = "assets/textures/player/player12.png"
player2 = "assets/textures/player/player21.png"
player2_moves = "assets/textures/player/player22.png"

breakable = choice([
                "assets/textures/blocks/derevaskawitch4uglblenia.png",
                "assets/textures/blocks/derevaskawitchuglblenie.png",
                "assets/textures/blocks/derewaska.png",
                "assets/textures/blocks/oboi.png",
                "assets/textures/blocks/seno.png"])

unbreakable = choice([
                "assets/textures/blocks/obsidian1.png",
                "assets/textures/blocks/obsidian2.png"])


font1 = font.SysFont("Arial", 35)
font2 = font.SysFont(('font/ariblk.ttf'), 60)

texture_size = 40
# це те скільки вийде блоків на екрані 40 кількість пікселів на оин силвол
level1_width = len(map_lvl1[0]) * texture_size
level1_height = len(map_lvl1) * texture_size

#розміри екрану
W = 1280
H = 720
pause_btn = TextureButton(1300, 20, 50, 50, "assets\\textures\\ui\\pause.png", font2)
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
        key_pressed = key.get_pressed()# задаєм в зміну значення
        if key_pressed[K_a]:# перевіряєм чи нажата кнопка це а
            self.rect.x -= self.speed# якщо так той демо в ліво
            # self.image = transform.scale(image.load(hero_l), (self.width, self.height))# підсьтавляєм фотку
            
        if key_pressed[K_d]:#кнопка в низ натиснута
            self.rect.x += self.speed# х додаєм швидкість рухаємось
            # self.image = transform.scale(image.load(hero_r), (self.width, self.height))#  підставляєм фотку
            
        if key_pressed[K_s]:# якщо в низ тобто в низ
            self.rect.y += self.speed# ми додає тобто спускаємось
            
        if key_pressed[K_w]:# якщо в верх то віднімаєм піднімаємось
            self.rect.y -= self.speed# 

def creating_lists_coordinate(list, x, y):
    list.append(tuple(x, y))
    return list


"""----------------------------------ФУНКЦІЇ------------------------------------------"""
x = 0
y = 0

def start_pos(map: None):# стартова позиція
    global items, hero, unbreakables, breakables, green_hides, dark_white_hides, enemys, texture_size, enemy_coordinates
    window.fill((116, 85, 2))
    pause_btn.draw(window)
    window.blit(text_life, (700, 10))


    breakables = list()
    unbreakables = list()
    green_hides = list()
    dark_white_hides = list()
    enemys = list()
    
    # всі списки дивіться в кінотеатрах(коді)
    x = 0#  координати для обєктів
    y = 0
    for r in map:# фор як раб почав ходити по списками перевіряєм індекси
        for c in r:#  стучим в двері перевіряєм чи
            if c == "b":# дім полу
                b = Settings(x,y, texture_size, texture_size, 0, breakable)# створюєм раба платформа
                breakables.append(b)
                items.add(b)
                if c == "u":
                    u = Settings(x, y, texture_size, texture_size, 0, breakable)
                    unbreakables.append(u)
                    items.add(u)
                if c == "g":
                    g = Settings(x, y,texture_size, texture_size, 0, breakable)
                    green_hides.append(g)
                    items.add(g)
                if c == "d":
                    d = Settings(x, y, texture_size, texture_size, 0, breakable)
                    dark_white_hides.append(d)
                    items.add(d)
                if c == "e":
                    enemy_coordinates = list()
                    enemy_coordinates = creating_lists_coordinate(enemy_coordinates, x, y)
                    print(enemy_coordinates)
                if c == "p":
                    hero = Player(300, 650, 50, 50 , 15, breakable)
                    pl_items.add(hero)
                if c == "l":
                    l = Settings(x, y, texture_size, texture_size, 0, breakable)
                if c == "|":
                    p = Settings(x, y, texture_size, texture_size, 0, breakable)
                    items.add(p)
            x += texture_size#  ікси плюс 40
        y += texture_size#  перміщаємось в низ
        x = 0#  ікси 0