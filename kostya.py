import pygame as pg
from maxym import TextureButton

font = pg.font.Font(None, 36)
back_button_from_htp = TextureButton(20, 760, 230, 100, "assets//textures//ui//back2.png")

def render_text_with_spacing(text, font, color, spacing):
    text_surface = pg.Surface((font.size(text)[0] + spacing * (len(text) - 1), font.size(text)[1]), pg.SRCALPHA)

    x_offset = 0

    for char in text:
        char_surface = font.render(char, True, color)
        text_surface.blit(char_surface, (x_offset, 0))
        x_offset += char_surface.get_width() + spacing

    return text_surface

window = pg.display.set_mode((0, 0), pg.FULLSCREEN)
W, H = pg.display.Info().current_w, pg.display.Info().current_h
background_image = pg.image.load(r'assets//textures//background.jpg')
background_image = pg.transform.scale(background_image, (W, H))

def display_rules(window):
    window.blit(background_image, (0, 0))
    
    rules = [
        "Складність гри можна змінити в налаштуваннях.",
        "Темні блоки не ломаються, лише білі!",
        "Правила гри: Відбивайтеся від ворожих танків, захищаючи свою базу!",
        "Гравець №1:",
        "Уверх - W",
        "Вниз - S",
        "Направо - D",
        "Наліво - A",
        "Стріляти - R",
    ]

    rules2 = [
        "Гравець №2:",
        "Уверх - стрілка уверх",
        "Вниз - стрілка вниз",
        "Направо - стрілка направо",
        "Наліво - стрілка наліво",
        "Стріляти - лівий ctrl"
    ]
    
    font_path = r"assets//textures//fonts//Blazma-Regular.otf"
    font_size = 36
    font = pg.font.Font(font_path, font_size)
    
    text_color = (255, 255, 255)
    letter_spacing = 1

    y_offset = 50
    for rule in rules:
        text = render_text_with_spacing(rule, font, text_color, letter_spacing)
        window.blit(text, (50, y_offset))
        y_offset += text.get_height() + 20

    y_offset2 = 230
    for rule in rules2:
        text = render_text_with_spacing(rule, font, text_color, letter_spacing)
        window.blit(text, (450, y_offset2))
        y_offset2 += text.get_height() + 20
    
    back_button_from_htp.draw(window)
    
    
    # вывод кнопки и текста на экран
    #button_rect = display_rules(window)
    # test coment 