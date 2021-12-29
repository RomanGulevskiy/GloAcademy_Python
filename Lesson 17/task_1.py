import random

def generate_secret_word():
    digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    secret_word = ''
    for i in range(4):
        random_index = random.randint(0, len(digits) - 1)
        secret_word += str(digits[random_index])
        digits.pop(random_index)
    return secret_word

def calc_bulls(user_word, secret_word):
    counter = 0
    for i in range(len(secret_word)):
        if user_word[i] == secret_word[i]:
            counter += 1
    return counter

def calc_cows(user_word, secret_word):
    counter = 0
    for i in range(len(secret_word)):
        if user_word[i] != secret_word[i] and user_word[i] in secret_word:
            counter += 1
    return counter

def is_valid_user_word(user_word, secret_word):
    if not user_word.isdigit():
        return False

    if len(user_word) != len(secret_word):
        return False

    for i in range(len(user_word)):
        if user_word.count(user_word[i]) == 1:
            return True
        else:
            return False

def play():
    secret_word = generate_secret_word()
    print('Угадайте число, загаданное компьютером!')
    print('Угадываемое число состоит из 4 уникальных цифр.')
    print('Вводимые числа также должны состоять из 4 уникальных цифр.')
    print()

    while True:
        user_word = input('Введите число: ')
        
        if not is_valid_user_word(user_word, secret_word):
            print('Ошибка ввода.')
            continue
        
        bulls = calc_bulls(user_word, secret_word)
        cows = calc_cows(user_word, secret_word)
        
        print('Угадано быков:', bulls, ', коров:', cows, '.')

        if bulls == 4:
            print('Поздравляем! Вы выиграли!')
            break
        
    play_again = input('Хотите сыграть еще раз? Да/Нет: ')

    if play_again.upper() == 'ДА':
        play()
    else:
        return

print('Добро пожаловать в игру "Быки и коровы"!')
play()