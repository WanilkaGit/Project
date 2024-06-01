map_lvlq1 = {
  "_________________",#Unbreakeble - u
  "|gggggggggggggggg/",#breakeable - b
  "|gb bbbb  bbbb bg/",#green_hide - g
  "|gb b  b  b  b bg/",#dark_white_hide - d
  "|gb bbbb  b  b bg/",#enemy - e
  "|gb    b  b  b bg/",#player1 - p
  "|gb bbbb  bbbb bg/",#lose - l
  "|gb  bb    bb  bg/",#win - w
  "|gb  bb bb bb  bg/",#кожен елемент цього
  "|gb    bbbb    bg/",#є частиню карти окрім
  "|gggggggggggggggg/",#пробілів
  "|u     b b      u/",#що вони означають написано вище
  "|g  b  bbb   b bg/",#теж зі знаком коментаря
  "|gb b  b b   b bg/",
  "|gb bu      ub bg/",
  "|gb b  bbb   b bg/",
  "|ggg   blb    gg /",
  "------------------"
}

x = 0
y = 0
def start_pos():# функція що розставляє все по стартових місцях
    global #все треба буде глобалізувати
    hero = Player(300, 650, 50, 50 , 15, hero_l)


    block_r = []# список 1:
    block_l = []# список 2:
    plat = []# список 3:
    
    # всі списки дивіться в кінотеатрах(коді)
    x = 0#  координати для обєктів
    y = 0
    for r in level1:# р дорівнює ряддку
        for c in r:#  с дорівнює символу з рядка р
            if c == "-":# дім полу
                p1 = Settings(x,y, 40, 40, 0, platform)# створюєм платформу спочатку координати, розмір, швидкість та картинка
                plat.append(p1)# додаємо до списку платформ
                items.add(p1)# додаємо до списку всього що є на карті
            if c == "|":# для лівої стіни
                p1 = Settings(x,y, 40, 40, 0, platform)# створюєм раба платформа
                plat.append(p1)# 
                items.add(p1)
            if c == "/":# для правої стіни
                p1 = Settings(x,y, 40, 40, 0, platform)# створюєм раба платформа
                plat.append(p1)# 
                items.add(p1)

            if c == "g":# для трави
                p1 = Settings(x,y, 40, 40, 0, platform)# створюєм раба платформа
                plat.append(p1)# 
                items.add(p1)

            if c == "b":# для кирпічної стіни
                p1 = Settings(x,y, 40, 40, 0, platform)# створюєм раба платформа
                plat.append(p1)# 
                items.add(p1)
              
            if c == "u":# для не взламної стіни
                p1 = Settings(x,y, 40, 40, 0, platform)# створюєм раба платформа
                plat.append(p1)# 
                items.add(p1)
 
            if c == "e":# для еміків
                p1 = Settings(x,y, 40, 40, 0, platform)# створюєм раба платформа
                plat.append(p1)# 
                items.add(p1)




            x += 40#  ікси плюс 40
        y += 40#  перміщаємось в низ
        x = 0#  ікси 0
    items.add(hero)
