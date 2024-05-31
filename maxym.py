import pygame as pg
from typing import Union, Optional, Tuple

class Button:
    '''Звичайна кнопка використовуй якщо не потрібна текстура і вона не має рухатися якщо фон не потрібен то пропусти введення його кольору'''
    def __init__(self, x: int, y: int, width: int, height: int, font: pg.font.Font, text: Union[str, bytes] = '', button_color: Optional[Tuple[int, int, int]] = None, text_color: Tuple[int, int, int] = (255, 255, 255)):
        self.rect = pg.Rect(x, y, width, height)
        self.color = button_color
        self.font = font
        self.text = text
        self.text_color = text_color
    
    #метод для відмальовки сюди треба вказати поверхню на якій буде малюватись кнопка pg.display також працює якщо що
    def draw(self, display: pg.Surface):
        '''Метод для відмальовки кнопки'''
        if self.color is not None: pg.draw.rect(display, self.color, self.rect)
        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        display.blit(text_surface, text_rect)

    #повертає bool в залежності від того пересікся курсор миші з кнопкою чи ні(так це тойже collidepoint але так як на мене зручніше)
    def is_pressed(self, pos: Tuple[int, int]) -> bool:
        '''повертає bool в залежності від того пересікся курсор миші з кнопкою чи ні(так це тойже collidepoint але так як на мене зручніше)'''
        return self.rect.collidepoint(pos)

class MovableButton:
    '''Кнопка яка більш придатна для руху використовуй якщо кнопка має рухатись та їй не потрібна текстура якщо фон кнопки непотрібен то пропусти введення кольору кнопки'''
    def __init__(self, width: int, height: int, font: pg.font.Font, text: Union[str, bytes] = '', button_color: Optional[Tuple[int, int, int]] = None, text_color: Tuple[int, int, int] = (255, 255, 255)):
        self.rect = pg.Rect(0, 0, 0, 0)
        self.width = width
        self.height = height
        self.color = button_color
        self.font = font
        self.text = text
        self.text_color = text_color

        #метод для відмальовки сюди треба вказати поверхню на якій буде малюватись кнопка pg.display також працює якщо що та також вказати x та y координати кнопки
    def draw(self, display: pg.Surface, x: int, y: int):
        '''Метод для відмальовки кнопки якщо тобы не треба щоб кнопка рухалась використовуй звичайний класс Button()'''
        self.rect = pg.Rect(x, y, self.width, self.height)
        if self.color is not None: pg.draw.rect(display, self.color, self.rect)
        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center= self.rect.center)
        display.blit(text_surface, text_rect)

    #повертає bool в залежності від того пересікся курсор миші з кнопкою чи ні(так це тойже collidepoint але так як на мене зручніше)
    def is_pressed(self, pos: Tuple[int, int]) -> bool:
        '''повертає bool в залежності від того пересікся курсор миші з кнопкою чи ні(так це тойже collidepoint але так як на мене зручніше)'''
        return self.rect.collidepoint(pos)

class TextureButton(pg.sprite.Sprite):
    '''Кнопка з підтримкою текстури вона наслідується від Sprite тобу має всі його функції для коректної відмальовки використовуй метод draw()'''
    def __init__(self, x: int, y: int, width: int, height: int, texture_path: str, font: pg.font.Font, text: Union[str, bytes] = '', text_color: Tuple[int, int, int] = (255, 255, 255)):
        super().__init__()
        self.image = pg.transform.scale(pg.image.load(texture_path), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.font = font
        self.text = text
        self.text_color = text_color
        self.text_surface = self.font.render(self.text, True, self.text_color)
        self.text_rect = self.text_surface.get_rect(center=self.rect.center)
    
    #метод для відмальовки сюди треба вказати поверхню на якій буде малюватись кнопка pg.display також працює якщо що
    def draw(self, display: pg.Surface):
        '''Метод для відмальовки кнопки. Використовуй його щоб текст також малювався на кнопці'''
        display.blit(self.image, self.rect)
        display.blit(self.text_surface, self.text_rect)
    
    #повертає bool в залежності від того пересікся курсор миші з кнопкою чи ні(так це тойже collidepoint але так як на мене зручніше)
    def is_pressed(self, pos: Tuple[int, int]) -> bool:
        '''повертає bool в залежності від того пересікся курсор миші з кнопкою чи ні(так це тойже collidepoint але так як на мене зручніше)'''
        return self.rect.collidepoint(pos)