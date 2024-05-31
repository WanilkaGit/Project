import pygame as pg
pg.init()
from maxym import Button

FPS = 60

font = pg.font.Font(None, 32)
display = pg.display.set_mode((0, 0), pg.FULLSCREEN)
pg.display.set_caption('Battle City')
back = pg.transform.scale(pg.image.load('fon1.jpg'), (1500, 1000))  #завантажуєемо картинку фона і розтягємо її у рзміри екрана
pg.display.set_icon(pg.image.load('fon1.jpg'))  #завантажуєемо фото іконки
pg.display.set_caption('Battle city') #даємо назву вікну додатка

### об'єкти кнопок ###
how_to_play_btn = Button(630, 200, 200, 80, font, 'How to play', (100, 10, 10))
play_btn = Button(630, 300, 200, 80, font, 'Play', (100, 10, 10))
setting_btn = Button(630, 400, 200, 80, font, 'Settings', (100, 10, 10))

game = True
clock = pg.time.Clock()

while game:
    display.blit(back, (0,0))

    # відмальовка кнопок #
    how_to_play_btn.draw(display)
    play_btn.draw(display)
    setting_btn.draw(display)
        

    for event in pg.event.get():

        if event.type == pg.QUIT:
            game = False


        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                game = False

        

    pg.display.update()

    clock.tick(FPS)
pg.quit()
