map_lvlq1 = {
  "_________________",#Unbreakeble - u
  "|gggggggggggggggg/",#breakeable - b
  "|gb bbbb  bbbb bg/",#green_hide - g
  "|gb b  b  b  b bg/",#dark_white_hide - d
  "|gb bbbb  b  b bg/",#enemy - e
  "|gb    b  b  b bg/",#player1 - p
  "|gb bbbb  bbbb bg/",#lose - l
  "|gb  bb    bb  bg/",#win - w
  "|gb  bb bb bb  bg/",
  "|gb    bbbb    bg/",
  "|gggggggggggggggg/",
  "|u     b b      u/",
  "|g  b  bbb   b bg/",
  "|gb b  b b   b bg/",
  "|gb bu      ub bg/",
  "|gb b  bbb   b bg/",
  "|ggg   blb    gg /",
  "------------------"
}

x = 0
y = 0
def start_pos():# стартова позиція
    global items, camera, hero, block_r, block_l, plat, coins, door, coin
    global stairs_lst, enemy_lst, p6, p11, p7, p8, open_d, open_ch, manas# робимо глобальними змінни
    hero = Player(300, 650, 50, 50 , 15, hero_l)


    block_r = []# список 1:
    block_l = []# список 2:
    plat = []# список 3:
    
    # всі списки дивіться в кінотеатрах(коді)
    x = 0#  координати для обєктів
    y = 0
    for r in level1:# фор як раб почав ходити по списками перевіряєм індекси
        for c in r:#  стучим в двері перевіряєм чи
            if c == "-":# дім полу
                p1 = Settings(x,y, 40, 40, 0, platform)# створюєм раба платформа
                plat.append(p1)# 
                items.add(p1)
            if c == "-":# дім полу
                p1 = Settings(x,y, 40, 40, 0, platform)# створюєм раба платформа
                plat.append(p1)# 
                items.add(p1)

            x += 40#  ікси плюс 40
        y += 40#  перміщаємось в низ
        x = 0#  ікси 0
    items.add(hero)
