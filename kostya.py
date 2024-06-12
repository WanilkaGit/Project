import pygame as pg
from maxym import TextureButton
#from ivan import window

def display_rules(window):
    window.fill((100, 100, 0))
    
    font = pg.font.Font(None, 36)
    
    rules = [
        "Правила гри: Отбивайтесь от вражеских танков защищая свою базу!",
        "Вверх - W",
        "Вниз - S",
        "Направо - D",
        "Налево - A",
        "Стрелять - R"
    ]
    
    y_offset = 50
    for rule in rules:
        text = font.render(rule, True, (255, 255, 255))
        window.blit(text, (50, y_offset))
        y_offset += 50
    
    pg.display.flip()
    back_button = TextureButton(630, 300, 200, 80, r"assets\textures\pngwing.com.png", font)

    # вывод кнопки и текста на экран
    button_rect = display_rules(window)
