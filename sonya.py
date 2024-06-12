import pygame as pg
from maxym import *
from ivan import window, font2


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

def setting():
    window.fill((116, 85, 2))
    title = font2.render('Налаштування', True, (0,0,0))
    btn1 = CheckButton(50, 150, 50, font2, 'Легкий')
    btn2 = CheckButton(250, 150, 50, font2, 'Середній')
    btn3 = CheckButton(450, 150, 50, font2, 'Важкий')
    btn = CheckButtonGroup(btn1, btn2, btn3)
    pg.display.flip()
    btn.update(window)
    window.blit(title, (500, 30))
