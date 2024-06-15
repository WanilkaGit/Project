"""------------------------------------Імпорта----------------------------------------"""
import time
from maxym import TextureButton
from random import choices, choice
from pygame import*# імпорт пайгейма
from oleksii import text_life
init()# ініціалізуєм пайгейм


"""------------------------------------Map build--------------------------------------"""
map_lvl1 = [
    "___________________________________________________",#Unbreakeble - u
    "|dddddddddddddddddddddddddddddddddu dbbbbbwbbbbbd |",#breakeable - b
    "|   bbbb  bbbb   udb bbbb  bbbb bdu  ddbbbbbbbdd  |",#green_hide - g
    "|u  b  b  b g u  udb bl b  b  b bdu    ddbbbdd    |",#dark_white_hide - d
    "|   bbbb  bbbb u udb bbbb  b  b bdu u   ddddd  u  |",#enemy - e
    "|   b  b   g b   udb    b  b  b bdu  d            |",#player1 - p
    "|   bbbb  bbbb   udb bbbb  bbbb bdu     u     g   |",#lose - l
    "|  u             udb            bdu   b    g      |",#win - w
    "|    bbbbbbbbbbb udb  bb bb bb  bdu     b      g  |",#кожен елемент цього
    "|     uuuu   gg  udb    bbbb    bdu d       u     |",#є частиню карти окрім
    "|  bbbg gg       uggggggggggggggggu   bbbb  bbbb  |",#пробілів
    "|  gg       buub uu     b  b     uu   b  b  b     |",#що вони означають написано вище
    "|    u  bub gggg ug  b  bbbb  b bgu   bbbb  bbbb  |",#теж зі знаком коментаря
    "|  bub  ggg      ugb b  b  b  b bgu      b     b  |",
    "|  ggg       bub ugb bu      ub bgu   bbbb  bbbb  |",
    "|       bbb  ggg ugb b  bbb   b bgu               |",
    "|       blb      uggg    ggggggggggggggggggggggggg|",
    "___________________________________________________"
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

pause_btn = TextureButton(1300, 20, 50, 50, "assets\\textures\\ui\\pause.png", font2)
# створюєм вікно
#window = pg.display.set_mode((0, 0), pg.FULLSCREEN)
#W, H = pg.display.Info().current_w, pg.display.Info().current_h

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

    def reset(self, window):# тут прописана функція ресет
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