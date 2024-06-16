"""------------------------------------Імпорта----------------------------------------"""
import time
from maxym import TextureButton
from random import choices, choice
from pygame import*# імпорт пайгейма
import pygame as pg

init()# ініціалізуєм пайгейм

window = pg.display.set_mode((0, 0), pg.FULLSCREEN)
W, H = pg.display.Info().current_w, pg.display.Info().current_h
background_image = pg.image.load(r'assets\textures\background.jpg')
background_image = pg.transform.scale(background_image, (W, H))

"""------------------------------------Map--------------------------------------"""
map_lvl1 = [
    "_________________",#Unbreakeble - u
    "|gggggggggggggggg|",#breakeable - b
    "|gbebbbbe bbbbebg|",#green_hide - g
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
    "|ggg  pblb    gg |",
    "__________________"
]


""" ----------------------------------ЗМІННІ-------------------------------------"""
move_player1 = 1
texture_size = 40
# це те скільки вийде блоків на екрані 40 кількість пікселів на оин силвол
level1_width = len(map_lvl1[0]) * texture_size
level1_height = len(map_lvl1) * texture_size


""" ----------------------------------ГРУПИ-------------------------------------"""
items = sprite.Group()#  створюємо тусу
players = sprite.Group()


"""----------------Картинки щоб швидше вставляти бо по іншому довго-------------------"""
player1 = "assets/textures/player/player11.png"
player1_moves = "assets/textures/player/player12.png"
players_image = [player1, player1_moves]

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

green_hide = "assets/textures/blocks/kuvsinka.png"


""" ----------------------------------ШРИФТИ-------------------------------------"""
font1 = font.SysFont("Arial", 35)
font2 = font.SysFont(('font/ariblk.ttf'), 60)


""" ----------------------------------Кнопки-------------------------------------"""
pause_btn = TextureButton(1300, 20, 50, 50, "assets\\textures\\ui\\pause.png", font2)
# створюєм вікно
#window = pg.display.set_mode((0, 0), pg.FULLSCREEN)
#W, H = pg.display.Info().current_w, pg.display.Info().current_h


"""-------------------------------------Класи---------------------------------------"""
class Blocks(sprite.Sprite):# основний клас тут основні параметри
    def __init__(self, x, y, width, height, speed, img, breaking_ables: bool, ghost_skills: bool):
        super().__init__()
        self.width = width
        self.height = height
        self.speed = speed
        self.image = transform.scale(image.load(img), (self.width, self.height))
        self.breaking_ables = breaking_ables
        self.ghost_skills = ghost_skills
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Player(Blocks):# клас гравця з супер класом сетінгс
    rotate = 0
    def update(self):# тут буде переміщення в право ліво
        global move_player1
        key_pressed = key.get_pressed()# задаєм в зміну значення

        if key_pressed[K_w]:# якщо в верх то віднімаєм піднімаємось
            self.rect.y -= self.speed#
            if move_player1 % 2 == 0:
                self.image = transform.scale(image.load(player1_moves), (self.width, self.height))# підсьтавляєм фотку
                move_player1 += 1
            else:
                self.image = transform.scale(image.load(player1), (self.width, self.height))# підсьтавляєм фотку
                move_player1 += 1

        if key_pressed[K_a]:# перевіряєм чи нажата кнопка це а
            self.rect.x -= self.speed# якщо так той демо в лівоdef move_animation():
            if move_player1 % 2 == 0:
                self.image = transform.scale(image.load(player1_moves), (self.width, self.height))# підсьтавляєм фотку
                move_player1 += 1
            else:
                self.image = transform.scale(image.load(player1), (self.width, self.height))# підсьтавляєм фотку
                move_player1 += 1

        if key_pressed[K_s]:# якщо в низ тобто в низ
            self.rect.y += self.speed# ми додає тобто спускаємось
            if move_player1 % 2 == 0:
                self.image = transform.scale(image.load(player1_moves), (self.width, self.height))# підсьтавляєм фотку
                move_player1 += 1
            else:
                self.image = transform.scale(image.load(player1), (self.width, self.height))# підсьтавляєм фотку
                move_player1 += 1

        if key_pressed[K_d]:#кнопка в низ натиснута
            self.rect.x += self.speed# х додаєм швидкість рухаємось
            # self.image = transform.scale(image.load(hero_r), (self.width, self.height))#  підставляєм фотку
            if move_player1 % 2 == 0:
                self.image = transform.scale(image.load(player1_moves), (self.width, self.height))# підсьтавляєм фотку
                move_player1 += 1
            else:
                self.image = transform.scale(image.load(player1), (self.width, self.height))# підсьтавляєм фотку
                move_player1 += 1

def creating_lists_coordinate(list, x, y):
    list.append((x, y))
    return list


"""----------------------------------ФУНКЦІЇ------------------------------------------"""
x = 0
y = 0

def start_pos(map: None):# стартова позиція
    global items, players, hero, unbreakables, breakables, green_hides, dark_white_hides, enemys, texture_size, enemy_coordinates

    breakables = list()
    unbreakables = list()
    green_hides = list()
    dark_white_hides = list()
    enemy_coordinates = []
    
    # всі списки дивіться в кінотеатрах(коді)
    x = 0#  координати для обєктів
    y = 0
    for r in map:# фор як раб почав ходити по списками перевіряєм індекси
        for c in r:#  стучим в двері перевіряєм чи
            if c == "b":# дім полу
                b = Blocks(x,y, texture_size, texture_size, 0, breakable, True, False)# створюєм раба платформа
                breakables.append(b)
                items.add(b)
            if c == "u":
                u = Blocks(x, y, texture_size, texture_size, 0, unbreakable, False, False)
                unbreakables.append(u)
                items.add(u)
            if c == "g":
                g = Blocks(x, y,texture_size, texture_size, 0, green_hide, False, True)
                green_hides.append(g)
                items.add(g)
            if c == "d":
                d = Blocks(x, y, texture_size, texture_size, 0, green_hide, False, True)
                dark_white_hides.append(d)
                items.add(d)
            if c == "e":
                enemy_coordinates = creating_lists_coordinate(enemy_coordinates, x, y)
                print(enemy_coordinates)
            if c == "p":
                hero = Player(x, y, 34, 34 , 1, player1, True, False)
                players.add(hero)
            if c == "l":
                l = Blocks(x, y, texture_size, texture_size, 0, breakable, False, False)
            if c == "|":
                p = Blocks(x, y, texture_size, texture_size, 0, breakable, False, False)
                items.add(p)
            x += texture_size#  ікси плюс 40
        y += texture_size#  перміщаємось в низ
        x = 0#  ікси 0
    return items