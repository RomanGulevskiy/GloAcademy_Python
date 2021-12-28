def is_valid_char(user_char):
    if user_char.isalpha():
        first_alphabet_char = 1072
        last_alphabet_char = 1103
        user_char = user_char.lower()
        if ord(user_char) >= first_alphabet_char and ord(user_char) <= last_alphabet_char:
            return True
        else:
            return False
    else:
        return False

def generate_user_word(secret_word):
    if secret_word.isalpha():
        return '*' * len(secret_word)
    else:
        return False

def update_user_word(user_word, secret_word, user_char):
    new_user_word = ''
    for i in range(len(secret_word)):
        if secret_word[i].lower() == user_char.lower():
            new_user_word += user_char.lower()
        else:
            new_user_word += user_word[i]

    return new_user_word

def play():
    question = 'форма письменности, основанная на стандартном наборе знаков.'
    secret_word = 'алфавит'
    user_word = generate_user_word(secret_word)
    user_chars = []
    counter = 0
    
    print('Загаданное слово:', question)
    print(user_word)
    print()

    while user_word != secret_word:
        user_char = input('Введите букву: ')
        if len(user_char) != 1 or not is_valid_char(user_char):
            print('Ошибка ввода')
            continue
    
        new_user_word = update_user_word(user_word, secret_word, user_char)
        if user_word == new_user_word:
            if user_char.lower() in user_chars:
                print('Вы уже называли эту букву.')
                continue
            user_chars.append(user_char.lower())
            counter += 1
            print('К сожалению, в этом слове нет такой буквы.')
        else:
            if user_char.lower() in user_chars:
                print('Вы уже называли эту букву.')
                continue
            user_chars.append(user_char.lower())
            counter += 1
            print('Поздравляем! Есть такая буква!')
        
        user_word = new_user_word   
        print(new_user_word)
    
    print('Поздравлям! Вы угадали слово полностью!')
    print('Вам понадобилось попыток:', counter, '.')

    play_again = input('Хотите сыграть еще раз? Да/Нет: ')   
    if play_again.upper() == 'ДА':
        play()
    else:
        return    

print('Добро пожаловать в игру "Поле чудес"!')
print()
play()