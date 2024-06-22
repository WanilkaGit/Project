import pygame as pg
from maxym import TextureButton

# Ініціалізуємо шрифт розміром 36
font = pg.font.Font(None, 36)

# Створюємо кнопку "Назад" із заданими координатами, розмірами та текстурою
back_button_from_htp = TextureButton(20, 760, 230, 100, "assets//textures//ui//back2.png")

# Функція для рендерингу тексту з більшим інтервалом між буквами
def render_text_with_spacing(text, font, color, spacing):
    # Створюємо поверхню для тексту з урахуванням додаткових пробілів
    text_surface = pg.Surface((font.size(text)[0] + spacing * (len(text) - 1), font.size(text)[1]), pg.SRCALPHA)

    x_offset = 0  # Початкове зміщення по X

    # Проходимо по кожному символу в рядку
    for char in text:
        # Рендеримо символ на окрему поверхню
        char_surface = font.render(char, True, color)
        # Копіюємо символ на основну поверхню тексту
        text_surface.blit(char_surface, (x_offset, 0))
        x_offset += char_surface.get_width() + spacing  # Зміщуємо координати для наступного символу

    return text_surface  # Повертаємо створену поверхню з текстом

# Створюємо вікно та налаштовуємо його на повноекранний режим
window = pg.display.set_mode((0, 0), pg.FULLSCREEN)
W, H = pg.display.Info().current_w, pg.display.Info().current_h  # Отримуємо розміри екрану
background_image = pg.image.load(r'assets//textures//background.jpg')  # Завантажуємо фонове зображення
background_image = pg.transform.scale(background_image, (W, H))  # Масштабуємо зображення під розмір екрану

# Функція для відображення правил гри
def display_rules(window):
    window.blit(background_image, (0, 0))  # Відображаємо фонове зображення
    
    rules = [  # Правила гри для першого гравця
        "Складність гри можна змінити в налаштуваннях.",
        "Темні блоки не ломаються, лише білі!",
        "Правила гри: Відбивайтеся від ворожих танків, захищаючи свою базу!",
        "Гравець №1:",
        "Уверх - W",
        "Вниз - S",
        "Направо - D",
        "Наліво - A",
        "Стріляти - E",
    ]

    rules2 = [  # Правила гри для другого гравця
        "Гравець №2:",
        "Уверх - стрілка уверх",
        "Вниз - стрілка вниз",
        "Направо - стрілка направо",
        "Наліво - стрілка наліво",
        "Стріляти - лівий ctrl"
    ]
    
    font_path = r"assets//textures//fonts//Blazma-Regular.otf"  # Шлях до файлу шрифту
    font_size = 36  # Розмір шрифту
    font = pg.font.Font(font_path, font_size)  # Ініціалізуємо шрифт
    
    text_color = (255, 255, 255)  # Колір тексту (білий)
    letter_spacing = 1  # Інтервал між літерами

    y_offset = 50  # Початкове зміщення по Y для першого набору правил
    for rule in rules:
        text = render_text_with_spacing(rule, font, text_color, letter_spacing)  # Рендеримо текст з інтервалами між літерами
        window.blit(text, (50, y_offset))  # Відображаємо текст на вікні
        y_offset += text.get_height() + 20  # Зміщуємо координати для наступного рядка

    y_offset2 = 230  # Початкове зміщення по Y для другого набору правил
    for rule in rules2:
        text = render_text_with_spacing(rule, font, text_color, letter_spacing)  # Рендеримо текст з інтервалами між літерами
        window.blit(text, (450, y_offset2))  # Відображаємо текст на вікні
        y_offset2 += text.get_height() + 20  # Зміщуємо координати для наступного рядка
    
    back_button_from_htp.draw(window)  # Відображаємо кнопку "Назад" на вікні

    
    
    # вывод кнопки и текста на экран
    #button_rect = display_rules(window)
    # test coment 