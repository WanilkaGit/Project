import pygame as pg
from maxym import *
from ivan import *


pg.init()

def main_menu():
    global setting_btn, how_to_play_btn, play_btn
    font = pg.font.Font(None, 32)
   
    pg.display.set_icon(pg.image.load('fon1.jpg'))  #завантажуєемо фото іконки
    pg.display.set_caption('Battle city') #даємо назву вікну додатка
         ### об'єкти кнопок ###
    how_to_play_btn = Button(630, 200, 200, 80, font, 'How to play', (100, 10, 10))
    play_btn = Button(630, 300, 200, 80, font, 'Play', (100, 10, 10))
    setting_btn = Button(630, 400, 200, 80, font, 'Settings', (100, 10, 10))
        # відмальовка об'єктів #
    how_to_play_btn.draw(window)
    play_btn.draw(window)
    setting_btn.draw(window)

    
def push_btn():
    press_set = setting_btn.is_pressed([630, 400])
    press_play = play_btn.is_pressed([630, 300])
    press_how_play = how_to_play_btn.is_pressed([630, 200])

    if press_set == True:
        setting()

    if press_play == True:
        start_pos()

    if press_how_play == True:
        pass

def setting():
    pass
