import math
import random

def find_optimal_attempts(limit):
    return math.ceil(math.log(limit, 2))

def is_valid_number(number, limit):
    if number.isdigit():
        if int(number) >= 1 and int(number) <= int(limit):
            return True
        else:
            return False
    else:
        return False

def is_valid_limit(number):
    if number.isdigit():
        if int(number) > 1:
            return True
        else:
            return False
    else:
        return False

def play():
    limit = input('Введите правую границу угадываемого числа (больше 1): ')

    while not is_valid_limit(limit):
        limit = input('Введите правую границу угадываемого числа (больше 1): ')
    
    secret_number = random.randint(1, int(limit))
    counter = 0
    
    while True:
        user_number = input('Введите число от 1 до ' + limit + ': ')
        
        if not is_valid_number(user_number, limit):
            continue
        else:
            user_number = int(user_number)
    
        if user_number < secret_number:
            counter += 1
            print('Загаданное число больше')
        elif user_number > secret_number:
            counter += 1
            print('Загаданное число меньше')
        else:
            counter += 1
            print('Поздравляем, вы угадали число!')
            print('Вам на это понадобилось попыток:', counter)
            print('Оптимальное количество попыток:', find_optimal_attempts(int(limit)))
            break

    play_again = input('Хотите сыграть еще раз? YES/NO: ')
    
    if play_again == 'YES':
        play()
    else:
        return

def play_ai():
    limit = input('Введите правую границу угадываемого числа (больше 1): ')
    while not is_valid_limit(limit):
        limit = input('Введите правую границу угадываемого числа (больше 1): ')

    user_number = input('Загадайте число от 1 до ' + limit + ': ')
    while not is_valid_number(user_number, limit):
        user_number = input('Загадайте число от 1 до ' + limit + ': ')
    user_number = int(user_number)

    start = 1
    finish = int(limit)
    counter = 0

    while True:
        number = (start + finish) // 2
        print('Компьютер считает, что вы загадали число:', number)

        choice = int(input('Компьютер угадал? 1 - Да, 2 - Загаданное число больше, 3 - Загаданное число меньше: '))
        while choice not in [1, 2, 3]:
            choice = int(input('Компьютер угадал? 1 - Да, 2 - Загаданное число больше, 3 - Загаданное число меньше: '))
        
        if number == user_number:
            print('Зачем вы обманываете компьютер? Ведь он уже угадал ваше число!')
            print('На это ему понадобилось попыток:', counter)
            print('Оптимальное количество попыток:', find_optimal_attempts(int(limit)))            
            break
        
        if choice == 2:
            counter += 1
            start = number + 1
        elif choice == 3:
            counter += 1
            finish = number
        else:
            counter += 1
            print(number)
            print('Компьютер отгадал ваше число!')
            print('На это ему понадобилось попыток:', counter)
            print('Оптимальное количество попыток:', find_optimal_attempts(int(limit)))
            break

    play_again = input('Хотите сыграть еще раз? YES/NO: ')
    
    if play_again == 'YES':
        play_ai()
    else:
        return

print('Добро пожаловать в игру "Угадай число"!')
game_type = int(input(('Выберите тип игры: 1 - Вы угадываете число, 2 - Компьютер угадывает число, 3 - Выход: ')))

while game_type not in [1, 2, 3]:
    game_type = int(input(('Выберите тип игры: 1 - Вы угадываете число, 2 - Компьютер угадывает число, 3 - Выход: ')))

if game_type == 1:
    play()
elif game_type == 2:
    play_ai()