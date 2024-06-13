import pygame as pg
from maxym import *
from ivan import window, font2
from oleksii import *


pg.init()

back_button = TextureButton(630, 400, 200, 80, "assets\\textures\\pngwing.com.png", font2)
start_button = TextureButton(630, 400, 100, 80, "assets\\textures\\blocks\\play.png", font2)
exit_to_main = TextureButton(430, 400, 100, 80, "assets\\textures\\blocks\\home.png", font2)
text_life = font2.render('Life: ' + str(hero_lives), (0,0,0))

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
    title2 = font2.render('Складність гри', True, (0,0,0))
    btn1 = CheckButton(50, 250, 50, font2, 'Легкий')
    btn2 = CheckButton(300, 250, 50, font2, 'Середній')
    btn3 = CheckButton(650, 250, 50, font2, 'Важкий')
    btn = CheckButtonGroup(btn1, btn2, btn3)
    back_button.draw(window)
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
