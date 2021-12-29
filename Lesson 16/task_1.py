def create_field():
    field = []
    for i in range(3):
        field.append(['*'] * 3)

    return field

def print_field(field):
    for i in range(3):
        for j in range(3):
            print(field[i][j], end='')
        print()

def check_win(field):
    for i in range(3):
        if field[i][0] != '*' and field[i][0] == field[i][1] == field[i][2]:
            return True

    for i in range(3):
        if field[0][i] != '*' and field[0][i] == field[1][i] == field[2][i]:
            return True

    if field[0][0] != '*' and field[0][0] == field[1][1] == field[2][2]:
        return True

    if field[0][2] != '*' and field[0][2] == field[1][1] == field[2][0]:
        return True

    return False

def check_end_game(field):
    if check_win(field):
        return True

    for i in range(3):
        for j in range(3):
            if field[i][j] == '*':
                return False

    return True

def is_valid_cell(row, column, field):
    if not row.isdigit() and not column.isdigit():
        return False
    elif int(row) not in [1, 2, 3] and int(column) not in [1, 2, 3]:
        return False
    elif field[int(row) - 1][int(column) - 1] != '*':
        return False    
    else:
        return True

def play():
    field = create_field()
    current_symbol = 'X'
    
    while not check_end_game(field):
        print()
        print_field(field)
        print()
        print('Сейчас ход:', current_symbol)
        row = input('Введите номер строки: ')
        column = input('Введите номер столбца: ')
    
        while not is_valid_cell(row, column, field):
            print('Ошибка ввода.')
            print('Такой ячейки не существует или ячейка уже занята')
            row = input('Введите номер строки: ')
            column = input('Введите номер столбца: ')
    
        row = int(row)
        column = int(column)
        field[row - 1][column - 1] = current_symbol
    
        if current_symbol == 'X':
            current_symbol = '0'
        else:
            current_symbol = 'X'
    
    print_field(field)
    if current_symbol == 'X':
        print('Игра окончена. Победа: 0')
    else:
        print('Игра окончена. Победа: X')
        
    play_again = input('Хотите сыграть еще раз? Да/Нет: ')

    if play_again.upper() == 'ДА':
        play()
    else:
        return

print('Добро пожаловать в игру "Крестики-нолики"!')
play()