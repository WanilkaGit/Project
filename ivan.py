"""------------------------------------Імпорта----------------------------------------"""
import time
from maxym import TextureButton
from random import choices, choice
from pygame import*# імпорт пайгейма
import pygame as pg

init()# ініціалізуєм пайгейм

#window = pg.display.set_mode((0, 0), pg.FULLSCREEN)
#W, H = pg.display.Info().current_w, pg.display.Info().current_h
#background_image = pg.image.load(r'assets\textures\background.jpg')
#background_image = pg.transform.scale(background_image, (W, H))

"""------------------------------------Map--------------------------------------"""
map_lvl1 = [
    "___________________________________________________",#Unbreakeble - u
    "|dddddddddddddddddddddddddddddddddu dbbbbbwbbbbbd |",#breakeable - b
    "|   bbbb  bbbb e udb bbbb  bbbb bdue ddbbbbbbbdd  |",#green_hide - g
    "|u  b  b  b g u eudb bl b  b  b bdu  e ddbbbdd    |",#dark_white_hide - d
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
    "|      pblb      uggg    ggggggggggggggggggggggggg|",
    "___________________________________________________"
]



""" ----------------------------------ЗМІННІ-------------------------------------"""
move_player1 = 1
texture_size = 32
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
def start_pos(map: None):# стартова позиція
    global items, players, hero, unbreakables, breakables, green_hides, dark_white_hides, texture_size, enemy_coordinates, empty_coordinates

    breakables = list()
    unbreakables = list()
    green_hides = list()
    dark_white_hides = list()
    enemy_coordinates = list()
    empty_coordinates = list()

    # всі списки дивіться в кінотеатрах(коді)
    x = 0#  координати для обєктів
    y = 70
    for r in map:# фор як раб почав ходити по списками перевіряєм індекси
        for c in r:#  стучим в двері перевіряєм чи
            if c == " ":
                empty_coordinates = creating_lists_coordinate(empty_coordinates, x, y)
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