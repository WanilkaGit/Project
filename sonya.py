import pygame as pg
from maxym import *
from ivan import window, font2, items
from oleksii import *
import time

pg.init()

font = pg.font.Font(None, 32)

### об'єкти кнопок ###

how_to_play_btn = Button(630, 200, 200, 80, font, 'How to play', (100, 10, 10))
play_btn = Button(630, 300, 200, 80, font, 'Play', (100, 10, 10))
setting_btn = Button(630, 400, 200, 80, font, 'Settings', (100, 10, 10))
exit_btn = Button(630, 500, 200, 80, font, 'Exit', (100, 10, 10))
constructor_button = Button(630, 700, 200, 80, font, 'Constructor', (100, 10, 10))

back_button_from_settings = TextureButton(630, 600, 100, 100, "assets\\textures\\ui\\back.png", font2)
start_button = TextureButton(630, 400, 100, 80, "assets\\textures\\ui\\play.png", font2)
exit_to_main = TextureButton(430, 400, 100, 80, "assets\\textures\\ui\\home.png", font2)

btn1 = CheckButton(50, 250, 50, font2, 'Легкий')
btn2 = CheckButton(300, 250, 50, font2, 'Середній')
btn3 = CheckButton(650, 250, 50, font2, 'Важкий')



def main_menu():
        # відмальовка об'єктів #
    how_to_play_btn.draw(window)
    play_btn.draw(window)
    setting_btn.draw(window)
    exit_btn.draw(window)
    constructor_button.draw(window)

def setting():
    window.fill((116, 85, 2))
    title = font2.render('Налаштування', True, (0,0,0))
    title2 = font2.render('Складність гри', True, (0,0,0))

    btn = CheckButtonGroup(btn1, btn2, btn3)
    back_button_from_settings.draw(window)
    btn.update(window)
    window.blit(title, (500, 30))
    window.blit(title2, (100, 100))

def pause():
    window.fill((116, 85, 2))
    title = font2.render('---Pause---', True, (0,0,0))
    title2 = font2.render('Рахунок: ', True, (0,0,0))
    title3 = font2.render('Життя: ', str(hero_lives), True, (0,0,0))
    window.blit(title,(500, 100))
    window.blit(title2,(300, 150))
    window.blit(title3,(300, 250))
    start_button.draw(window)
    exit_to_main.draw(window)
