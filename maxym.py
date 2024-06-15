import pygame as pg
from random import randint, choice
from typing import Union, Optional, Tuple
import json
pg.font.init()
font = pg.font.Font(None, 32)

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
        pg.draw.rect(display, self.color, self.rect)
        pg.draw.rect(display, (255, 255, 255), self.mini_rect)
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
        if not is_on_screen(self, 800, 800):
            self.kill()
            del self
    
    #я зробив це просто томущо іван попросив може буде корисно
    def set_position(self, x: int, y: int):
        '''Переміщує танк на вказані координати'''
        self.rect.x = x
        self.rect.y = y
  
    def new(self, dir: int):
        '''робить новий екземпляр классу Bullet на основі себе'''

        new_bullet = Bullet(self.image, self.speed, self.damage)
        new_bullet.dir = dir #dir це direction тобіш напрямок якщо хтось не зрозумів
        new_bullet.image = pg.transform.rotate(new_bullet.image, 90 * dir)
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
    
    '''
    def __init__(self, texture: pg.Surface, speed: Union[int, float], agility: int, firing_rate: int, health: Union[int, float], score: int, bullet: Bullet, blocks: pg.sprite.Group):
        super().__init__()
        self.original_texture = texture
        self.image = texture
        self.rect = self.image.get_rect()
        self.speed = speed
        self.agility = agility
        self.firing_rate = firing_rate
        self.score = score
        self.health = health
        self.bullet = bullet
        self.dir = 1 #dir це direction тобіш напрямок якщо хтось не зрозумів
        self.blocks = blocks
        self.bullets = pg.sprite.Group()

    def __random_rotate(self):
        '''повертає танк в одному з чотирьох напрямків'''        
        self.dir = randint(1,4)
        self.image = pg.transform.rotate(self.original_texture, 90 * self.dir - 90)

    def __collide(self):
        '''колізія ворога зі стінами чі краєм карти'''
        
        #записуємо всі блоки з якими стикнувся танк в змінну collided_blocks якщо список не пустий перевіряємо колізію
        collided_blocks = pg.sprite.spritecollide(self, self.blocks, False)
        if collided_blocks:
            block = collided_blocks[0] #нам вистачає тільки першого блока зі списку
            if not block.ghost_skills:
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
        if self.rect.right > 800:
            self.rect.x = 800 - self.rect.width
            self.__random_rotate()
        elif self.rect.left < 0:
            self.rect.x = 0
            self.__random_rotate()
        if self.rect.bottom > 800:
            self.rect.y = 800 - self.rect.height
            self.__random_rotate()
        elif self.rect.top < 0:
            self.rect.y = 0
            self.__random_rotate()
        
    def update(self, display: pg.Surface):
        '''оновлює стан ворога та відмалюовує його на вказаній поверхні'''

        #тут генеруємо випадкове число якщо воно рівне одиниці то танк повертається в випадковому напрямці
        if randint(0, self.agility) == 1:
            self.__random_rotate()

        #тут генеруємо випадкове число якщо воно рівне одиниці то танк зробить постріл
        if randint(0, self.firing_rate) == 1:
            new_bullet = self.bullet.new(self.dir)
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
        
        self.__collide() #перевірка всіх потрібних зіткнень

        #оновлюємо позицію пулі та якщо вона пересікається з self.blocks то видаляємо і те і те
        self.bullets.update(display)
        collides = pg.sprite.groupcollide(self.bullets, self.blocks, False, False)
        for bullet, blocks in collides.items():
            for block in blocks:
                if not block.ghost_skills:
                    if block.breaking_ables:
                        block.kill()
                    bullet.kill()
    
    def take_damage(self, damage: Union[int, float]):
        '''Функція для нанесення шкоди ворогу якщо кількість життів ворога дорівнює нулю то видаляємо ворога'''
        self.health -= damage
        if self.health <= 0:
            self.kill()
            del self #del видаляє обєкт повністю замість вбудованного збирача сміття в пайтоні я роблю це провсяк випадок

    def new(self, pos: Tuple[int, int]):
        '''робить новий екземпляр классу Enemy на основі себе'''

        new_enemy = Enemy(self.image, self.speed, self.agility, self.firing_rate, self.health, self.score, self.bullet, self.blocks)
        new_enemy.rect.x = pos[0]; new_enemy.rect.y = pos[1]
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
    def __init__(self, enemys: list, spawns: Union[list, tuple] = ((100, 50), (500, 50), (750,50)), enemy_group: Optional[pg.sprite.Group] = None) -> None:
        self.enemys = enemys
        self.spawns = spawns

        #якщо при створенні вказано enemy_group то присвоюємо її до властивості self.enemy_group інакше робимо нову enemy_group
        if enemy_group is not None: self.enemy_group = enemy_group
        else: self.enemy_group = pg.sprite.Group()

    def spawn(self):
        '''спавнить і видаляє ворога зі списку'''
        
        #якщо список не пустий ми записуємо в змінну enemy перший елемент цього списку та видаляємо його піся чого додаємо enemy до группи enemy_group
        if self.enemys: 
            enemy = self.enemys.pop(0)
            self.enemy_group.add(enemy.new(choice(self.spawns)))
    
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
                self.enemy_group.add(enemy.new(choice(self.spawns)))
            else: #інакще виконуємо цей блок коду
                enemy = choice(self.enemys)
                self.enemy_group.add(enemy.new(choice(self.spawns)))

    def update(self, display):
        '''функція для оновлення стану всіх ворогів заспавнених цим спавнером'''
        self.enemy_group.update(display)

'''------------------------------------------------------просто функції----------------------------------------------------------------------------------------'''

def is_on_screen(sprite: pg.sprite.Sprite, screen_width: int, screen_height: int) -> bool:
    '''перевіряє чи знаходиться хоч один піксель обєкта у вказанному діапазоні'''
    return sprite.rect.right > 0 and sprite.rect.left < screen_width and sprite.rect.bottom > 0 and sprite.rect.top < screen_height

#так я її вже не використовую але подумав що нехай буде
def is_edge_touched(sprite: pg.sprite.Sprite, screen_width: int, screen_height: int) -> bool:
    '''перевіряє чі виходить обєкт за межі екрану хоч на піксель'''
    return sprite.rect.right >= screen_width or sprite.rect.left <= 0 or sprite.rect.bottom >= screen_height or sprite.rect.top <= 0

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

choice_block = 0
redacted = False

brekable_button = TextureButton(1300, 100, 64, 64, 'assets\\textures\\blocks\\derewaska.png')
unbrekable_button = TextureButton(1300, 200, 64, 64, 'assets\\textures\\blocks\\obsidian2.png')
save_map_button = Button(80, 730, 200, 80, font, 'Зберегти', (100, 10, 10))

constructor_blocks = pg.sprite.Group()

canvas = pg.rect.Rect(81, 81, 639, 639)

def save_map():
        row = []
        block_map = []
        for y in range(2, 18):
            row = []
            tronul = False
            for x in range(2,18):
                for block in constructor_blocks:
                    if block.rect.collidepoint(x * 40 , y * 40):
                        tronul = True
                        row.append(block.label)
                if not tronul:
                    row.append(' ')
                tronul = False
            block_map.append(row)
        for row in block_map:
            print(f'{row},')
        with open('map.json', 'w') as file:
            json.dump(block_map, file)

from ivan import start_pos

#сцена конструктора
def map_constructor(display: pg.Surface):
    global choice_block, redacted, constructor_blocks
    mouse_pos = pg.mouse.get_pos()
    display.fill((0,0,0))
    pg.draw.rect(display, (100,100,100), canvas)
    if pg.mouse.get_pressed()[0]:
        redacted = True
        if brekable_button.is_pressed(mouse_pos):
            choice_block = 1
        elif unbrekable_button.is_pressed(mouse_pos):
            choice_block = 2


        if canvas.collidepoint(mouse_pos):
            for constructor_block in constructor_blocks:
                if constructor_block.rect.collidepoint(round_step(mouse_pos[0], 40), round_step(mouse_pos[1], 40)):
                    constructor_block.kill()
            if choice_block == 1:
                block = ConstructorBlock(round_step(mouse_pos[0], 40), round_step(mouse_pos[1], 40), 40, 40, 'assets\\textures\\blocks\\derewaska.png', 'b')
                constructor_blocks.add(block)
            elif choice_block == 2:
                block = ConstructorBlock(round_step(mouse_pos[0], 40), round_step(mouse_pos[1], 40), 40, 40, 'assets\\textures\\blocks\\obsidian2.png', 'u')
                constructor_blocks.add(block)
        
    elif pg.mouse.get_pressed()[2]:
        redacted = True
        for constructor_block in constructor_blocks:
                if constructor_block.rect.collidepoint(round_step(mouse_pos[0], 40), round_step(mouse_pos[1], 40)):
                    constructor_block.kill()
        
    elif pg.key.get_pressed()[pg.K_s] and redacted:
        row = []
        block_map = []
        for y in range(2, 18):
            row = []
            tronul = False
            for x in range(2,18):
                for block in constructor_blocks:
                    if block.rect.collidepoint(x * 40 , y * 40):
                        tronul = True
                        row.append(block.label)
                if not tronul:
                    row.append(' ')
                tronul = False
            block_map.append(row)
        for row in block_map:
            print(f'{row},')
        redacted = False
        with open('map.json', 'w') as file:
            json.dump(block_map, file)
    elif pg.key.get_pressed()[pg.K_l] and redacted:
        with open('map.json', 'r') as file:
            block_map = json.load(file)
            file.close()
        constructor_blocks = start_pos(block_map)

    brekable_button.draw(display)
    unbrekable_button.draw(display)
    constructor_blocks.draw(display)
    save_map_button.draw(display)