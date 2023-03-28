def game_deck():
    print('  0 1 2')
    for i in range(len(deck)):
        print(str(i), *deck[i])


def input_player_data():
    while True:
        data = input('Введите координаты через пробел: ').split()
        if (len(data)) != 2:
            print('Ошибка. Введено не две координаты')
            continue
        if not (data[0].isdigit() and data[1].isdigit()):
            print('Ошибка. Введите числа')
            continue
        x, y = map(int, data)
        if not (0 <= x <= 2 and 0 <= y <= 2):
            print('Ошибка. Введены координаты вне диапазона')
            continue
        if deck[x][y] != '-':
            print('Клетка уже занята')
            continue
        return x, y


def win_check():
    def line_check(x1, x2, x3, pl):
        if x1 == pl and x2 == pl and x3 == pl:
            return True

    for i in range(3):
        if line_check(deck[i][0], deck[i][1], deck[i][2], player) or \
                line_check(deck[0][i], deck[1][i], deck[2][i], player) or \
                line_check(deck[0][0], deck[1][1], deck[2][2], player) or \
                line_check(deck[2][0], deck[0][2], deck[1][1], player):
            return True


deck = [['-'] * 3 for _ in range(3)]
count = 0
while True:
    game_deck()
    if count % 2 == 0:
        player = 'x'
    else:
        player = 'o'
    if count == 9:
        print('Ничья')
        break
    x, y = input_player_data()
    deck[x][y] = player
    if win_check():
        game_deck()
        print('Победа игрока №', count % 2 + 1)
        break
    count += 1
