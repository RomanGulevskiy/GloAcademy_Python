import random

def is_valid_number(number):
    if number.isdigit():
        if int(number) > 0:
            return True
        else:
            return False
    else:
        return False

def asq_question(question):
    answer = input(question + ' Введите Да или Нет: ')
    while answer.upper() != 'ДА' and answer.upper() != 'НЕТ':
        print('Ошибка ввода')
        answer = input(question + ' Введите Да или Нет: ')    
    if answer.upper() == 'ДА':
        return True
    else:
        return False

def generate_password_params():
    print('Пожалуйста ответьте на несколько вопросов.')

    charset = ''
    digits = '0123456789'
    symbols = '!#$%&*+-=?@^_'
    cyrillic_uppercase = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    cyrillic_lowercase = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    latin_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    latin_lowercase = 'abcdefghijklmnopqrstuvwxyz'
    
    length = input('Какой длины должен быть пароль? ')
    while not is_valid_number(length):
        print('Ошибка ввода')
        length = input('Какой длины должен быть пароль? ')
    length = int(length)
    
    digits_enabled = asq_question('Исользовать в пароле цифры?')
    
    symbols_enabled = asq_question('Исользовать в пароле специальные символы?')
    
    cyrillic_uppercase_enabled = asq_question('Исользовать в пароле русские прописные буквы?')
    
    cyrillic_lowercase_enabled = asq_question('Исользовать в пароле русские строчные буквы?')
    
    latin_uppercase_enabled = asq_question('Исользовать в пароле латинские прописные буквы?')
    
    latin_lowercase_enabled = asq_question('Исользовать в пароле латинские строчные буквы?')
    
    if digits_enabled:
        charset += digits
        
    if symbols_enabled:
        charset += symbols
            
    if cyrillic_uppercase_enabled:
        charset += cyrillic_uppercase
    
    if cyrillic_lowercase_enabled:
        charset += cyrillic_lowercase
    
    if latin_uppercase_enabled:
        charset += latin_uppercase
    
    if latin_lowercase_enabled:
        charset += latin_lowercase    
    
    return length, charset
    
def generate_password(length, charset):
    if len(charset) > 0:
        password = ''
        for i in range(length):
            random_index = random.randint(0, len(charset) - 1)
            password += charset[random_index]
        return password
    else:
        return 'Вы не выбрали ни один набор символов для генерации пароля.'

def start():
    number_of_passwords = input('Сколько паролей вы хотите сгенерировать? ')
    while not is_valid_number(number_of_passwords):
        print('Ошибка ввода')
        number_of_passwords = input('Сколько паролей вы хотите сгенерировать? ')
    number_of_passwords = int(number_of_passwords)

    password_params = generate_password_params()

    for i in range(number_of_passwords):
        length = password_params[0]
        charset = password_params[1]
        password = generate_password(length, charset)
        print(password)
        
    do_repeat = input('Сгенерировать еще? Введите Да или Нет: ')
    while do_repeat.upper() != 'ДА' and do_repeat.upper() != 'НЕТ':
        print('Ошибка ввода')
        do_repeat = input('Сгенерировать еще? Введите Да или Нет: ')
    if do_repeat.upper() == 'ДА':
        start()
    else:
        return
        
print('Добро пожаловать в генератор паролей!')
start()






