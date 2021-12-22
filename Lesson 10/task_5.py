c1 = input('Введите строчную букву латинского алфавита: ')
c2 = input('Введите строчную букву латинского алфавита: ')

if ord(c1) >= 97 and ord(c1) <= 122 and ord(c2) >= 97 and ord(c2) <= 122:
    if ord(c1) > ord(c2):
        for c in range(ord(c2), ord(c1) + 1):
            print(chr(c), end=' ')
    else:
        for c in range(ord(c1), ord(c2) + 1):
            print(chr(c), end=' ')
else:
    print('Ошибка ввода')
