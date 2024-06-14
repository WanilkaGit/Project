import pygame as pg
from maxym import TextureButton

font = pg.font.Font(None, 36)
back_button_from_htp = TextureButton(630, 300, 100, 100, "assets\\textures\\ui\\back.png")

def display_rules(window):
    window.fill((100, 100, 0))
    
    rules = [
        "Складність гри можна обрати в налаштуваннях",
        "Темні блоки - не ламаютья, світлі можна зламати. ",
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
    
    back_button_from_htp.draw(window)

    pg.display.flip()
    
    
    # вывод кнопки и текста на экран
    #button_rect = display_rules(window)
