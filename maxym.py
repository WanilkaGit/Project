import pygame as pg
from random import randint, choice
from typing import Union, Optional, Tuple, List
import json
pg.font.init()
pg.init()

font = pg.font.Font('assets/textures/fonts/Blazma-Regular.otf', 24)

'''-----------------------------------------------------------усе пов'язане з кнопками--------------------------------------------------------------'''

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
        if self.color is not None: pg.draw.rect(display, self.color, self.rect) #якщо колір не вказано то немалюємо саму кнопку
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
        if self.color is not None: pg.draw.rect(display, self.color, self.rect) #якщо колір не вказано то немалюємо саму кнопку
        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center= self.rect.center)
        display.blit(text_surface, text_rect)

    #повертає bool в залежності від того пересікся курсор миші з кнопкою чи ні(так це тойже collidepoint але так як на мене зручніше)
    def is_pressed(self, pos: Tuple[int, int]) -> bool:
        '''повертає bool в залежності від того пересікся курсор миші з кнопкою чи ні(так це тойже collidepoint але так як на мене зручніше)'''
        return self.rect.collidepoint(pos)

class TextureButton(pg.sprite.Sprite):
    '''Кнопка з підтримкою текстури вона наслідується від Sprite тобу має всі його функції для коректної відмальовки використовуй метод draw()'''
    def __init__(self, x: int, y: int, width: int, height: int, texture_path: str, font: Optional[pg.font.Font] = None, text: Union[str, bytes] = '', text_color: Tuple[int, int, int] = (255, 255, 255)):
        super().__init__()
        self.image = pg.transform.scale(pg.image.load(texture_path), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        if font is not None:
            self.font = font
            self.text = text
            self.text_color = text_color
            self.text_surface = self.font.render(self.text, True, self.text_color)
            self.text_rect = self.text_surface.get_rect(center=self.rect.center)
        else: self.font = None
    
    #метод для відмальовки сюди треба вказати поверхню на якій буде малюватись кнопка pg.display також працює якщо що
    def draw(self, display: pg.Surface):
        '''Метод для відмальовки кнопки. Використовуй його щоб текст також малювався на кнопці'''
        display.blit(self.image, self.rect)
        if self.font is not None: display.blit(self.text_surface, self.text_rect)
    
    #повертає bool в залежності від того пересікся курсор миші з кнопкою чи ні(так це тойже collidepoint але так як на мене зручніше)
    def is_pressed(self, pos: Tuple[int, int]) -> bool:
        '''повертає bool в залежності від того пересікся курсор миші з кнопкою чи ні(так це тойже collidepoint але так як на мене зручніше)'''
        return self.rect.collidepoint(pos)

class ButtonGroup:
    '''
    Клас для створення гриппи кнопок

    при створенні вкажи кнопки які будуть до нього входити через кому

    для відмальовки кнопок використовуй метод draw() цього классу

    також є метод check_group_pressed він повертає натиснуту кнопку я не знаю навщо зробив його
    '''
    def __init__(self, *buttons: Union[Button, TextureButton]):
        self.buttons = buttons
    
    def draw(self, display: pg.Surface):
        for button in self.buttons:
            button.draw(display)
    
    def check_group_pressed(self, pos):
        for button in self.buttons:
            if button.rect.collidepoint(pos):
                return button

class CheckButton:
    '''
    Клас для перемикача сам по собі існувати не може для нормальної функціональності його треба додати до представника классу CheckButtonGroup
    '''
    def __init__(self, x: int, y: int, size: int, font: pg.font.Font, text: Union[str, bytes] = '', button_color: Tuple[int, int, int] = (0, 0, 0), text_color: Optional[Tuple[int, int, int]] = None):

        self.rect = pg.Rect(x, y, size, size)

        mini_size = size / 1.3
        self.mini_rect = pg.Rect(0, 0, mini_size, mini_size)
        self.mini_rect.center = self.rect.center

        status_size = size / 1.5
        self.status_rect = pg.Rect(0, 0, status_size, status_size)
        self.status_rect.center = self.mini_rect.center

        self.color = button_color
        self.font = font
        self.text = text
        self.text_color = text_color if text_color is not None else button_color
        self.button_pressed = False
    
    #метод для відмальовки сюди треба вказати поверхню на якій буде малюватись кнопка pg.display також працює якщо що
    def draw(self, display: pg.Surface):
        '''Метод для відмальовки кнопки'''
        pg.draw.rect(display, self.color, self.rect, 6)
        #pg.draw.rect(display, (255, 255, 255), self.mini_rect)
        if self.button_pressed: pg.draw.rect(display, self.color, self.status_rect)
        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.midbottom)
        text_rect.y += 9
        display.blit(text_surface, text_rect)

    #цей метод існує тільки для більшої читабельності коду в методі update в классі CheckButtonGroup
    def is_pressed(self, pos: Tuple[int, int]) -> bool:
        '''
        повертає bool в залежності від того пересікся курсор миші з кнопкою чи ні
        
        а взагалі цей метод тобі не потрібен викликай замість нього метод update в классі CheckButtonGroup
        '''
        return self.rect.collidepoint(pos)

class CheckButtonGroup:
    '''
    Клас для створення гриппи перемикачів

    при створенні вкажи перемикачі які будуть до нього входити через кому

    для відмальовки і перевірки натискання всіх кнопок достатньо визвати метод апдейт в екземпляру цього классу
    '''
    def __init__(self, *buttons: CheckButton):
        self.buttons = []
        for button in buttons:
            self.buttons.append(button)

    def update(self, display: pg.Surface):
        '''
        відмальовує кнопки та перевіряє яка кнопка була натиснута

        статус кнопки зберігається в змінній button_pressed
        
        '''
        for button in self.buttons:
            button.draw(display)
        if pg.mouse.get_pressed()[0]:
            for button in self.buttons:
                if button.is_pressed(pg.mouse.get_pos()):
                    for button in self.buttons:
                        button.button_pressed = False
                        if button.is_pressed(pg.mouse.get_pos()):
                            button.button_pressed = True
                    break

class LineEdit:
    '''
    Класс для лайн едіту

    Посуті це строка в якій коритувач може вводити текст +- як в консолі через input() але прямо в грі

    з першими чотирьма п'ятьма я думаю все зрозуміло

    max_symbol - максимальна кількість символів яку може ввести користувач якщо поставити 0 то можна писати нескінченну кількість символів

    з text_color я думаю все зрозуміло

    focused_color цей колір буде мати лайнедіт якщо він використовується якщо його не вказувати то лайнедіт буде прозорим

    unfocused_color - колір який буде мати лайнедіт якщо він не використовується якщо його не вказувати і при цьому вказаний focused_color то він буде мати його колір якщо хочеш щоб лайнедіт був прозорий то не вказуй focused_color

    frame_size - розміри рамок лайн едіта якщо поставити 0 то фон буде суцільним
    '''
    def __init__(self, x: int, y: int, width: int, height: int, font: pg.font.Font, max_symbol: int, text_color: Tuple[int, int, int], focused_color: Optional[Tuple[int, int, int]] = None, unfocused_color: Optional[Tuple[int, int, int]] = None, hint_color: Optional[Tuple[int, int, int]] = None, hint: str = '',  frame_size: int = 4):
        self.rect = pg.Rect(x, y, width, height)
        self.color = focused_color
        self.unactive_color = unfocused_color
        self.frame_size = frame_size
        self.text_color = text_color
        self.hint_color = hint_color
        self.font = font
        self.max_symbol = max_symbol
        self.hint = hint

        self.flash = 25

        self.focused = False
        self.text = ''
        self.final_text = self.text
        self.line_text = self.font.render(self.text, True, self.text_color)

    def update(self, event: pg.event.Event):
        '''посуті просто викликає методи check_focus та keys_update так код просто виглядає більш гарно і при цьому функціонал в раз потреби легко розділити'''
        self.check_focus(event)
        self.text_update(event)

    def check_focus(self, event: pg.event.Event):
        '''функція яка перевіряє чі натиснув гравець на лайн едіт і якщо так то focused = True інакще focused = False може бути користна якщо ти хочеш переписати функціонал text_update'''
        if event.type == pg.MOUSEBUTTONDOWN: # якщо кнопка мищі натиснута
            if self.rect.collidepoint(event.pos): # якщо курсор мищі знаходиться при цьому на лайн едіті
                self.focused = True
            else: # інакше
                self.focused = False
                self.line_text = self.font.render(self.text, True, self.text_color)

    def text_update(self, event: pg.event.Event):
        '''оновлює текст в лайн едіти може бути користно якщо вам не потрібен функціонал check_focus або ви хочете його переробити'''
        if self.focused and event.type == pg.KEYDOWN: # якщо натиснута клавіща на кравіатурі
                if event.key == pg.K_BACKSPACE: #якщо натиснуто бекспейс (дога стрілочка назад в углу клавіатури)
                    self.flash = 24 # виставляємо цю змінну на 24 щоб користувачу було легше орієнтуатись
                    self.text = self.text[:-1] # видаляємо останній символ в строці
                elif event.key == pg.K_ESCAPE: # якщо натиснуту ескейп
                    self.focused = False
                    self.line_text = self.font.render(self.text, True, self.text_color)
                elif event.key == pg.K_RETURN or event.key == pg.K_KP_ENTER: # якщо натиснуто ентер або ентер на нупад клавіатурі
                    self.focused = False
                    self.line_text = self.font.render(self.text, True, self.text_color)
                    self.final_text = self.text
                elif event.key == pg.K_DELETE: #якщо натиснуто деліт
                    self.text = ''
                else: # якщо натиснута люба інша клавіша на клавіатурі
                    if event.unicode not in {'/t'}:
                        if self.max_symbol != 0: # якщо максимальна кількість символів не дорівнює нулю (це зроблено для того щоб олзробник міг виставити безкінечну кількість символів)
                            if len(self.text) <= self.max_symbol:
                                self.text += event.unicode
                                self.flash = 24 # виставляємо цю змінну на 24 щоб користувачу було легше орієнтуатись
                        else: # інакще не перевіряємо скільки символів написав користувач
                            self.text += event.unicode
                            self.flash = 24 # виставляємо цю змінну на 24 щоб користувачу було легше орієнтуатись

    def draw(self, display: pg.Surface):
        '''малює лайн едіт на екрані'''
        if self.focused: # якщо лайн едіт активний
            if self.flash <= 20: # якщо ця зміння менше або дорівнює двадцяти то не відмальовуємо оцю палицю в кінці тексту
                self.line_text = self.font.render(self.text, True, self.text_color)
            else: # інакше відмальовуємо цю саму палицю
                self.line_text = self.font.render(self.text + '|', True, self.text_color)
                if self.flash >= 40: # якщо ця змінна більше або дорівню сорок то скидуємо її на нуль
                    self.flash = 0
            self.flash += 1
        elif self.text == '':
            self.line_text = self.font.render(self.hint, True, self.hint_color)

        if self.color is not None: # якщо був встановлений колір то відмальовує прямокутник
            if self.focused: # якщо лайн едіт активний то відмальовуємо прямокутник з активним кольором
                pg.draw.rect(display, self.color, self.rect, self.frame_size)
            elif self.unactive_color is not None: # якщо лайн едіт не активний і неактивний колір задано то відмальовуємо прямокутник з неактивним кольором
                pg.draw.rect(display, self.unactive_color, self.rect, self.frame_size)
            else: # якщо неактивний колір не задано і при цьому задано активний колір то відмальовуємо прямокутни з звичайним(активним) кольором
                pg.draw.rect(display, self.color, self.rect, self.frame_size)

        display.blit(self.line_text, (self.rect.x + 5, self.rect.y + 5))
                
'''-------------------------------------------------усе пов'язане з танками------------------------------------------------------------------------------------------'''

#цей класс підходить і для кулі гравця
class Bullet(pg.sprite.Sprite):
    '''
    Простий клас кулі яка летить в заданому напрямку та ламає стіни з якими стикається
    
    texture - це має бути екземпляр класу Surface

    тобто її треба робити за таким шаблоном ім'я_текстури = pg.image.load(шлях_до_спрайта.тип_його_файлу)

    speed - швидкість кулі за кадр в пікселях

    damage - шкада яку задає куля ворогу при влучанні
    '''
    def __init__(self, texture: pg.Surface, speed: Union[int, float], damage: Union[int, float]):
        super().__init__()
        self.image = texture
        self.rect = self.image.get_rect()
        self.speed = speed
        self.damage = damage
        self.dir = 0 #dir це direction тобіш напрямок якщо хтось не зрозумів
        self.zone = (0, 70, 1500, 900)

    def update(self, display: pg.Surface):
        '''оновлює позицію кулі та відальовує її на вказаній поверхні'''

        #в залежності від значення dir куля летить в потрібну сторону
        #не придумав як це автоматизувати тому тут така гілка з іфів
        if self.dir == 1:
            self.rect.y -= self.speed
        elif self.dir == 2:
            self.rect.x -= self.speed
        elif self.dir == 3:
            self.rect.y += self.speed
        elif self.dir == 4:
            self.rect.x += self.speed
        display.blit(self.image, self.rect)

        #якщо куля не на карті то видаляємо її
        #del видаляє обєкт повністю замість вбудованного збирача сміття в пайтоні я роблю це провсяк вмпадок
        if is_edge_touched(self, self.zone[0], self.zone[1], self.zone[2], self.zone[3]):
            self.kill()
            del self
    
    #я зробив це просто томущо іван попросив може буде корисно
    def set_position(self, x: int, y: int):
        '''Переміщує танк на вказані координати'''
        self.rect.x = x
        self.rect.y = y

    def new(self, dir: int, zone: Tuple[int, int, int, int]):
        '''робить новий екземпляр классу Bullet на основі себе'''

        new_bullet = Bullet(self.image, self.speed, self.damage)
        new_bullet.dir = dir #dir це direction тобіш напрямок якщо хтось не зрозумів
        new_bullet.image = pg.transform.rotate(new_bullet.image, 90 * dir)
        new_bullet.zone = zone
        return new_bullet

#dir це direction тобіш напрямок якщо хтось не зрозумів

class Enemy(pg.sprite.Sprite):
    '''
    основний класс ворога
    
    texture - це має бути екземпляр класу Surface

    тобто його треба робити за таким шаблоном ім'я_текстури = pg.image.load(шлях_до_спрайта.тип_його_файлу)
    
    speed - швидкість танку за кадр в пікселях

    agility - шанс що танк в цьому кадрі повернеться чим менше agility тим частіше танк буде обертатись
    
    якщо дорівнює 0 то танк повертається тільки коли стикається зі стіною

    firing_rate - шанс що танк в цьому кадрі зробить постріл чим менше firing_rate тим частіше танк буде стріляти

    якщо дорівнює 0 то танк не буде стріляти

    health - кількість життів в танка

    blocks - сюди треба вказати группу блоків танк буде оброблювати усі зіткнення саме з цією группою
    
    zone вписувати тут не треба!!!!!!!!
    '''
    def __init__(self, textures: Union[List[pg.Surface], Tuple[pg.Surface, pg.Surface]], speed: Union[int, float], agility: int, firing_rate: int, health: Union[int, float], score: int, bullet: Bullet, blocks: pg.sprite.Group, players: pg.sprite.Group, bases: pg.sprite.Group, zone: Tuple[int, int, int, int] = (0, 70, 1200, 900)):
        super().__init__()
        self.original_texture1, self.original_texture2  = textures
        self.texture1, self.texture2 = self.original_texture1, self.original_texture2
        self.image = textures[0]
        self.rect = self.image.get_rect()
        self.speed = speed
        self.agility = agility
        self.firing_rate = firing_rate
        self.score = score
        self.health = health
        self.bullet = bullet
        self.dir = 1 #dir це direction тобіш напрямок якщо хтось не зрозумів
        self.blocks = blocks
        self.base_list = bases
        self.players = players
        self.bullets = pg.sprite.Group()
        self.frame = 0

        self.min_x, self.min_y, self.max_x, self.max_y = zone

    def __animate(self):
        if self.frame <= 2:
            self.image = self.texture1
        else:
            self.image = self.texture2
            if self.frame >= 4: self.frame = -1
        self.frame += 1

    def __random_rotate(self):
        '''повертає танк в одному з чотирьох напрямків'''        
        self.dir = randint(1,4)
        self.texture1 = pg.transform.rotate(self.original_texture1, 90 * self.dir - 90)
        self.texture2 = pg.transform.rotate(self.original_texture2, 90 * self.dir - 90)

    def __collide(self):
        '''колізія ворога зі стінами чі краєм карти'''
        
        #записуємо всі блоки з якими стикнувся танк в змінну collided_blocks якщо список не пустий перевіряємо колізію
        collided_blocks = pg.sprite.spritecollide(self, self.blocks, False)
        if collided_blocks:
            block = collided_blocks[0] #нам вистачає тільки першого блока зі списку
            if self.dir == 1:
                self.rect.top = block.rect.bottom
            elif self.dir == 2:
                self.rect.left = block.rect.right 
            elif self.dir == 3:
                self.rect.bottom = block.rect.top      
            elif self.dir == 4:
                self.rect.right = block.rect.left

            self.__random_rotate() 

        #тут перевіряємо чі знаходиться танк на карті (константи треба змінити в майбутньому)
        if self.rect.right > self.max_x:
            self.rect.x = self.max_x - self.rect.width
            self.__random_rotate()
        elif self.rect.left < self.min_x:
            self.rect.x = self.min_x
            self.__random_rotate()
        if self.rect.bottom > self.max_y:
            self.rect.y = self.max_y - self.rect.height
            self.__random_rotate()
        elif self.rect.top < self.min_y:
            self.rect.y = self.min_y
            self.__random_rotate()
        
    def update(self, display: pg.Surface):
        '''оновлює стан ворога та відмалюовує його на вказаній поверхні'''

        #тут генеруємо випадкове число якщо воно рівне одиниці то танк повертається в випадковому напрямці
        if randint(0, self.agility) == 1:
            self.__random_rotate()

        #тут генеруємо випадкове число якщо воно рівне одиниці то танк зробить постріл
        if randint(0, self.firing_rate) == 1:
            new_bullet = self.bullet.new(self.dir, (self.min_x, self.min_y, self.max_x, self.max_y))
            new_bullet.rect.center = self.rect.center
            self.bullets.add(new_bullet)

        display.blit(self.image, self.rect)

        #тан їде в ту або іншу сторону в залешності від значення dir
        if self.dir == 1:
            self.rect.y -= self.speed
        elif self.dir == 2:
            self.rect.x -= self.speed
        elif self.dir == 3:
            self.rect.y += self.speed
        elif self.dir == 4:
            self.rect.x += self.speed

        self.__animate()
        
        self.__collide() #перевірка всіх потрібних зіткнень

        #оновлюємо позицію пулі та якщо вона пересікається з self.blocks то видаляємо і те і те
        self.bullets.update(display)
        collides = pg.sprite.groupcollide(self.bullets, self.blocks, False, False)
        for bullet, blocks in collides.items():
            for block in blocks:
                    if block.breaking_ables:
                        block.kill()
                    bullet.kill()

        collides = pg.sprite.groupcollide(self.bullets, self.players, True, False)
        if collides:
            for bullet, players in collides.items():
                players[0].new_live()

        collides = pg.sprite.spritecollide(self, self.players, False)
        if collides:
            collides[0].new_live()
            self.take_damage(1)
            del self

        collides = pg.sprite.groupcollide(self.bullets, self.base_list, True, False)
        if collides:
            for bullet, base_list in collides.items():
                if base_list:
                    base_list[0].kill()
    
    def take_damage(self, damage: Union[int, float]):
        '''Функція для нанесення шкоди ворогу якщо кількість життів ворога дорівнює нулю то видаляємо ворога'''
        self.health -= damage
        if self.health <= 0:
            self.kill()
            del self #del видаляє обєкт повністю замість вбудованного збирача сміття в пайтоні я роблю це провсяк випадок

    def new(self, pos: Tuple[int, int], zone: Tuple[int, int, int, int]):
        '''робить новий екземпляр классу Enemy на основі себе'''
 
        new_enemy = Enemy((self.original_texture1, self.original_texture2), self.speed, self.agility, self.firing_rate, self.health, self.score, self.bullet, self.blocks, self.players, self.base_list, zone)
        new_enemy.rect.x, new_enemy.rect.y = pos
        return new_enemy

#при виклику методу spawn() в классі EnemySpawner просто одразу спавниться ворог 
#я зробив це для того щоб було легше прописувати різну логіку спавну для різних рівнів
#
#наприклад так:
#last_call_time = pg.time.get_ticks()
#random_interval = 100
#
#і в ігровому циклі:
#current_time = pg.time.get_ticks()
#if current_time - last_call_time > random_interval:
#    назва_спавнеру.spawn()
#    last_call_time = current_time
#    random_interval = randint(900, 2500)
#
#або так:
#if randint(0, 200) == 1:
#   назва_спавнеру.spawn()

class EnemySpawner:
    '''
    клас для спавну ворогів
    
    enemys - cписок ворогів вони будуть спавнитись по черзі при виклику spawn()
    
    записувати так (екземпляр_класу_ворога, екземпляр_класу_ворога) екземпляри класу ворога можна записувати до нескінченсті коли вони закінчуться вороги перестануть з'являтися

    spawns - список можливих місць спавну ворогів
    
    записувати так ((координата_X,координата_Y)) таких списків в цьому списку може бути скільки завгодно

    enemy_group - це группа спрайтів сюди можна вказати любу группу але це придназначено для группи ворогів

    якщо нічого не вказувати то класс зробить свою группу ворогів але тоді до неї буде складніше отримати доступ і оновлювати доведеться через цей класс
    '''
    def __init__(self, enemys: list, spawns: Union[list, tuple] = ((100, 50), (500, 50), (750,50)), enemy_group: Optional[pg.sprite.Group] = None, zone: Tuple[int, int, int, int] = (0, 0, 1200, 900)) -> None:
        self.original_enemys = enemys.copy()
        self.enemys = enemys.copy()
        self.spawns = spawns

        self.zone = zone

        #якщо при створенні вказано enemy_group то присвоюємо її до властивості self.enemy_group інакше робимо нову enemy_group
        if enemy_group is not None: self.enemy_group = enemy_group
        else: self.enemy_group = pg.sprite.Group()

    def spawn(self):
        '''спавнить і видаляє ворога зі списку'''

        #якщо список не пустий ми записуємо в змінну enemy перший елемент цього списку та видаляємо його піся чого додаємо enemy до группи enemy_group
        if self.enemys: 
            enemy = self.enemys.pop(0)
            self.enemy_group.add(enemy.new(choice(self.spawns), self.zone))
    
    def spawn_random(self, del_enemy_from_list: bool = False):
        '''
        Функція для спавну ворогів в рандомному порядку
        
        якщо del_enemy_from_list дорівнює True то метод spawn_random буде пряцювати также як і метод spawn але порядок буде випадковий

        також просто хотів додати примітку що чим більше ворогів одного типу
        тим більше шанс що заспавниться саме цей тип тобіш наприклад якщо в enemys буде передано
        [enemy1, enemy1, enemy1, enemy2] то шанс що заспавниться enemy1 75% а щанс на
        спавн enemy2 25%
        '''
        #перевіряємо чи є в списку self.enemys хоч один елемент
        if self.enemys:
            if del_enemy_from_list: #якщо вибрана опція видаляти ворога зі списку при спавні то виконуємо цей блок
                enemy = self.enemys.pop(randint(0, len(self.enemys) - 1))
                self.enemy_group.add(enemy.new(choice(self.spawns),  self.zone))
            else: #інакще виконуємо цей блок коду
                enemy = choice(self.enemys)
                self.enemy_group.add(enemy.new(choice(self.spawns), self.zone))

    def reset_enemys(self):
        self.enemy_group.empty()
        self.enemys = self.original_enemys.copy()

    def change_enemy_list(self, new_enemys: list):
        self.original_enemys = new_enemys.copy()
        self.enemys = new_enemys.copy()

    def update(self, display):
        '''функція для оновлення стану всіх ворогів заспавнених цим спавнером'''
        self.enemy_group.update(display)

'''------------------------------------------------------просто функції----------------------------------------------------------------------------------------'''

def is_on_screen(sprite: pg.sprite.Sprite, screen_width: int, screen_height: int) -> bool:
    '''перевіряє чи знаходиться хоч один піксель обєкта на екрані розміри екрану треба задавати самому для більшоюї гібкості'''
    return sprite.rect.right > 0 and sprite.rect.left < screen_width and sprite.rect.bottom > 0 and sprite.rect.top < screen_height

def is_on_zone(sprite: pg.sprite.Sprite, zone_begin_x, zone_begin_y, zone_x, zone_y) -> bool:
    '''перевіряє чи знаходиться хоч один піксель обєкта у вказанному діапазоні'''
    return sprite.rect.right > zone_begin_x and sprite.rect.left < zone_x and sprite.rect.bottom > zone_begin_y and sprite.rect.top < zone_y

#так я її вже не використовую але подумав що нехай буде
def is_edge_touched(sprite: pg.sprite.Sprite, zone_begin_x, zone_begin_y, zone_x, zone_y) -> bool:
    '''перевіряє чі виходить обєкт за межі екрану хоч на піксель'''
    return sprite.rect.right >= zone_x or sprite.rect.left <= zone_begin_x or sprite.rect.bottom >= zone_y or sprite.rect.top <= zone_begin_y

def round_step(num, step):
    return round((num - step / 2) / step) * step

'''---------------------------------------------------------сцени-------------------------------------------------------------------------------------------'''

class ConstructorBlock(pg.sprite.Sprite):
    def __init__(self, x: int, y: int, width: int, height: int, texture: str, label: str):
        super().__init__()
        self.label = label
        self.image = pg.transform.scale(pg.image.load(texture), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self, display: pg.Surface):
        display.blit(self.image, self.rect)

class ConstructorLabel(pg.sprite.Sprite):
    def __init__(self, x: int, y: int, width: int, height: int, label: str, font: pg.font.Font):
        super().__init__()
        self.label = label
        self.font = font
        self.image = pg.Surface((0, 0))
        self.rect = pg.rect.Rect(x, y, width, height)

    def draw(self, display: pg.Surface):
        text_surface = self.font.render(self.label, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=self.rect.center)
        display.blit(text_surface, text_rect)

class MaxymsScenes:
    def __init__(self):
        self.choice_block = 0
        self.constructor_blocks = pg.sprite.Group()
        self.game_blocks = pg.sprite.Group()
        self.hides_blocks = pg.sprite.Group()
        self.players = pg.sprite.Group()
        self.bases = pg.sprite.Group()
        self.spawner = EnemySpawner([], zone = (64, 64, 576, 576))

        self.d_w, self.d_h = pg.display.Info().current_w, pg.display.Info().current_h
        self.background = pg.transform.scale(pg.image.load('assets/textures/background.jpg'), (self.d_w,self.d_h))

        self.last_call_time = 0
        self.interval = 250

        # Оголошення кнопок і інших об'єктів тут, але їх ініціалізація в конструкторі класу

        self.brekable_button = TextureButton(1300, 100, 64, 64, 'assets/textures/blocks/derewaska.png')
        self.unbrekable_button = TextureButton(1300, 200, 64, 64, 'assets/textures/blocks/obsidian2.png')
        self.green_hide_button = TextureButton(1300, 300, 64, 64, 'assets/textures/blocks/kuvsinka.png')
        self.base_button =  TextureButton(1300, 400, 64, 64, 'assets/textures/blocks/base.png')

        self.enemy_spawn_point_button = Button(1100, 100, 170, 64, font, 'спавн ворога', (100, 100, 100))
        self.player_spawn_point_button = Button(1100, 200, 170, 64, font, 'спавн гравця', (100, 100, 100))

        self.main_menu_button = Button(1, 1, 180, 70, font, 'Назад в меню', (100, 10, 10))

        self.save_map_button = Button(80, 730, 200, 80, font, 'Зберегти', (100, 10, 10))
        self.load_map_button = Button(300, 730, 200, 80, font, 'Завантажити', (100, 10, 10))
        self.map_name_line = LineEdit(300, 20, 280, 40, font, 12, (255,255,255), (150, 150, 150), (100, 100, 100), (100, 100, 100), 'введи назву карти', 5)
        self.play_constructor_button = Button(520, 730, 200, 80, font, 'Грати', (100, 10, 10))
        self.reset_button = Button(1300, 730, 200, 80, font, 'Очистити карту', (100, 10, 10))

        self.constructor_buttons = ButtonGroup(self.brekable_button, self.unbrekable_button, self.green_hide_button,
                                               self.enemy_spawn_point_button, self.player_spawn_point_button,
                                               self.main_menu_button, self.save_map_button, self.load_map_button,
                                               self.play_constructor_button, self.reset_button, self.base_button)

        self.save_slot1_name = 'save1'
        self.save_slot2_name = 'save2'
        self.save_slot3_name = 'save3'
        self.save_slot4_name = 'save4'

        self.save_slot1 = Button(100, 100, 200, 80, font, self.save_slot1_name, (100, 10, 10))
        self.save_slot2 = Button(600, 100, 200, 80, font, self.save_slot2_name, (100, 10, 10))
        self.save_slot3 = Button(100, 600, 200, 80, font, self.save_slot3_name, (100, 10, 10))
        self.save_slot4 = Button(600, 600, 200, 80, font, self.save_slot4_name, (100, 10, 10))

        self.load_slot1 = Button(100, 100, 200, 80, font, self.save_slot1_name, (100, 10, 10))
        self.load_slot2 = Button(600, 100, 200, 80, font, self.save_slot2_name, (100, 10, 10))
        self.load_slot3 = Button(100, 600, 200, 80, font, self.save_slot3_name, (100, 10, 10))
        self.load_slot4 = Button(600, 600, 200, 80, font, self.save_slot4_name, (100, 10, 10))

        self.back_to_constructor_button = Button(600, 0, 200, 85, font, 'Відмінити', (100, 10, 10))

        self.back_to_constructor_from_test_button = Button(1100, 100, 350, 85, font, 'Повернутись до створення', (100, 10, 10))

        self.save_map_buttons = ButtonGroup(self.save_slot1, self.save_slot2, self.save_slot3, self.save_slot4,
                                            self.back_to_constructor_button)
        self.load_map_buttons = ButtonGroup(self.load_slot1, self.load_slot2, self.load_slot3, self.load_slot4,
                                            self.back_to_constructor_button)

        self.tile_size = 40
        self.canvas = pg.rect.Rect(81, 81, 639, 639)

    def map_to_list(self, map_: pg.sprite.Group):
        '''ковертує карту в конструкторі в список'''
        block_map = [] #підготовуємо чистий список для карти
        for y in range(2, 18):
            row = [] # кожну ітерацію цього циклу очищуємо змінну row
            tronul = False # кожну ітерацію цього циклу змінюємо tronul на False
            for x in range(2, 18):
                for block in map_: # перебираємо всі блоки в надії що хоч один є на цих координатах
                    if block.rect.collidepoint(x * self.tile_size, y * self.tile_size): #якщо в цьому місці є блок то tronul стає True і в row записується мітка блоку
                        tronul = True
                        row.append(block.label)
                if not tronul: # якщо на координатах не було блоку до додаємо в row пробіл
                    row.append(' ')
                tronul = False # коли переберемо всі блоки на координатах tronul має бути False
            block_map.append(row)
        return block_map

    def check_provisos(self):
        players_in_map = 0
        enemys_is_in_map = 0
        bases_is_in_map = 0
        have_map_name = 0

        block_map = self.map_to_list(self.constructor_blocks)
        
        if self.map_name_line.text != '':
            have_map_name += 1

        for row in block_map:
            for block in row:
                if block == 'p':
                    players_in_map += 1
                elif block == 'e':
                    enemys_is_in_map += 1
                elif block == 'l':
                    bases_is_in_map += 1

        if players_in_map == 1 and enemys_is_in_map and bases_is_in_map and have_map_name: return True

        else: return False
        


    def save_map(self, save_slot: str):
        '''зберігає карту в обраний слот, якщо слотів нема створює їх'''
        block_map = self.map_to_list(self.constructor_blocks) # конвертуємо карту з конструктора карт в список
        try:
            with open('assets//data//maps.json', 'r') as file: # якщо такий файл існує то відкриваємо його і записуємо його в змінну data
                data = json.load(file)
                file.close()
        except FileNotFoundError:  # інекше записуємо в змінну data шаблон того як все має бути
            data = {
                'save_slot1': [[]],
                'save_slot1_name': 'save1',
                'save_slot2': [[]],
                'save_slot2_name': 'save2',
                'save_slot3': [[]],
                'save_slot3_name': 'save3',
                'save_slot4': [[]],
                'save_slot4_name': 'save4'
            }

        with open('assets//data//maps.json', 'w') as file: # тут просто змінюємо вміст слота та завантажуємо data в файл
            data[save_slot] = block_map
            data[save_slot+'_name'] = self.map_name_line.text
            json.dump(data, file)
            file.close()

    def load_constructor_map(self, save_slot: str):
        '''завантажує карту з обраного слоту якщо слота не уснує нічого не робить'''
        try:
            with open('assets//data//maps.json', 'r') as file: #відкриваємо файл
                data = json.load(file)
                block_map = data[save_slot] # карта дорівнює карті з обраного слоту
                self.map_name_line.text = data[save_slot + '_name']
            x = 80
            y = 80
            self.constructor_blocks = pg.sprite.Group() #очищуємо стару карту

            for row in block_map: # тут усім знайомуй алгоритм
                for block in row:
                    if block == 'b':
                        block = ConstructorBlock(x, y, self.tile_size, self.tile_size,
                                                 'assets//textures//blocks//derewaska.png', 'b')
                        self.constructor_blocks.add(block)
                    elif block == 'u':
                        block = ConstructorBlock(x, y, self.tile_size, self.tile_size,
                                                 'assets//textures//blocks//obsidian2.png', 'u')
                        self.constructor_blocks.add(block)
                    elif block == 'g':
                        block = ConstructorBlock(x, y, self.tile_size, self.tile_size,
                                                 'assets//textures//blocks//kuvsinka.png', 'g')
                        self.constructor_blocks.add(block)
                    elif block == 'l':
                        block = ConstructorBlock(x, y, self.tile_size, self.tile_size,
                                                 'assets//textures//blocks//base.png', 'l')
                        self.constructor_blocks.add(block)
                    elif block == 'e':
                        block = ConstructorLabel(x, y, self.tile_size, self.tile_size, 'e', font)
                        self.constructor_blocks.add(block)
                    elif block == 'p':
                        block = ConstructorLabel(x, y, self.tile_size, self.tile_size, 'p', font)
                        self.constructor_blocks.add(block)
                    x += self.tile_size
                y += self.tile_size
                x = 80
        except FileNotFoundError: # якщо слоту не існує просто нічого не робимо
            pass
    def load_slots_names(self):
        try:
            with open('assets//data//maps.json', 'r') as file: #відкриваємо файл
                data = json.load(file)
                self.save_slot1.text = data['save_slot1_name']
                self.save_slot2.text = data['save_slot2_name']
                self.save_slot3.text = data['save_slot3_name']
                self.save_slot4.text = data['save_slot4_name']
                self.load_slot1.text = data['save_slot1_name']
                self.load_slot2.text = data['save_slot2_name']
                self.load_slot3.text = data['save_slot3_name']
                self.load_slot4.text = data['save_slot4_name']
                file.close()
        except FileNotFoundError:
                self.save_slot1.text = self.save_slot1_name
                self.save_slot2.text = self.save_slot2_name
                self.save_slot3.text = self.save_slot3_name
                self.save_slot4.text = self.save_slot4_name
                self.load_slot1.text = self.save_slot1_name
                self.load_slot2.text = self.save_slot2_name
                self.load_slot3.text = self.save_slot3_name
                self.load_slot4.text = self.save_slot4_name
        


    # Методи для сцен (map_constructor, map_constructor_uninit, save_map_scene, load_map_scene, constructor_play) тут

    def map_constructor(self, display: pg.Surface): # scene = 5
        '''сцена з конструктором карт'''
        mouse_pos = pg.mouse.get_pos()
        display.blit(self.background, (0,0))
        pg.draw.rect(display, (100, 100, 100), self.canvas)
        if pg.mouse.get_pressed()[0]:
            if self.brekable_button.is_pressed(mouse_pos):
                self.choice_block = 1
            elif self.unbrekable_button.is_pressed(mouse_pos):
                self.choice_block = 2
            elif self.green_hide_button.is_pressed(mouse_pos):
                self.choice_block = 3
            elif self.base_button.is_pressed(mouse_pos):
                self.choice_block = 4
            elif self.enemy_spawn_point_button.is_pressed(mouse_pos):
                self.choice_block = 5
            elif self.player_spawn_point_button.is_pressed(mouse_pos):
                self.choice_block = 6

            if self.canvas.collidepoint(mouse_pos):
                for constructor_block in self.constructor_blocks:
                    if constructor_block.rect.collidepoint(round_step(mouse_pos[0], self.tile_size),
                                                          round_step(mouse_pos[1], self.tile_size)) and self.choice_block > 0:
                        constructor_block.kill()
                if self.choice_block == 1:
                    block = ConstructorBlock(round_step(mouse_pos[0], self.tile_size),
                                             round_step(mouse_pos[1], self.tile_size), self.tile_size, self.tile_size,
                                             'assets//textures//blocks//derewaska.png', 'b')
                    self.constructor_blocks.add(block)
                elif self.choice_block == 2:
                    block = ConstructorBlock(round_step(mouse_pos[0], self.tile_size),
                                             round_step(mouse_pos[1], self.tile_size), self.tile_size, self.tile_size,
                                             'assets//textures//blocks//obsidian2.png', 'u')
                    self.constructor_blocks.add(block)
                elif self.choice_block == 3:
                    block = ConstructorBlock(round_step(mouse_pos[0], self.tile_size),
                                             round_step(mouse_pos[1], self.tile_size), self.tile_size, self.tile_size,
                                             'assets//textures//blocks//kuvsinka.png', 'g')
                    self.constructor_blocks.add(block)
                elif self.choice_block == 4:
                    block = ConstructorBlock(round_step(mouse_pos[0], self.tile_size),
                                             round_step(mouse_pos[1], self.tile_size), self.tile_size, self.tile_size,
                                             'assets//textures//blocks//base.png', 'l')
                    self.constructor_blocks.add(block)
                elif self.choice_block == 5:
                    block = ConstructorLabel(round_step(mouse_pos[0], self.tile_size),
                                             round_step(mouse_pos[1], self.tile_size), self.tile_size, self.tile_size,
                                             'e', font)
                    self.constructor_blocks.add(block)
                elif self.choice_block == 6:
                    block = ConstructorLabel(round_step(mouse_pos[0], self.tile_size),
                                             round_step(mouse_pos[1], self.tile_size), self.tile_size, self.tile_size,
                                             'p', font)
                    self.constructor_blocks.add(block)

        elif pg.mouse.get_pressed()[2]:
            for constructor_block in self.constructor_blocks:
                if constructor_block.rect.collidepoint(round_step(mouse_pos[0], self.tile_size),
                                                      round_step(mouse_pos[1], self.tile_size)):
                    constructor_block.kill()

        self.constructor_buttons.draw(display)
        self.map_name_line.draw(display)
        for block in self.constructor_blocks:
            block.draw(display)

    def map_constructor_uninit(self):
        '''викликати при закритті конструктора карт для нормального функціонування'''
        self.choice_block = 0
        self.constructor_blocks = pg.sprite.Group()

    def save_map_scene(self, display: pg.Surface): # scene = 7
        '''сцена де вас питають куди збкрігати карту'''
        self.choice_block = 0
        display.fill((0, 0, 0))
        self.save_map_buttons.draw(display)

    def load_map_scene(self, display: pg.Surface): # scene = 8
        '''сцена де вас питають звідки завантажити карту'''
        self.choice_block = 0
        display.fill((0, 0, 0))
        self.load_map_buttons.draw(display)

    def constructor_play(self, display: pg.Surface): # scene = 9
        '''сцена де ти можеш протестувати тещо ти побудував в сцені з конструктором карт'''
        from ivan import bullets
        display.blit(self.background, (0,0))
        pg.draw.rect(display, (50, 50, 50), (64, 64, 512, 512))

        self.players.update(display)
        self.spawner.update(display)

        self.players.draw(display)
        self.game_blocks.draw(display)
        self.hides_blocks.draw(display)
        self.bases.draw(display)
        bullets.draw(display)

        current_time = pg.time.get_ticks()
        if current_time - self.last_call_time > self.interval:
            self.last_call_time = current_time
            self.spawner.spawn_random()
            self.interval = randint(500, 3500)

        self.back_to_constructor_from_test_button.draw(display)

maxyms_scenes = MaxymsScenes()