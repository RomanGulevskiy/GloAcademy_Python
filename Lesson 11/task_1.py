num = int(input('Введите число строк: '))
strings = []

if num > 0:
    for i in range(num):
        strings.append(input('Введите строку: '))

    needle = input('Введите поисковый запрос: ')
    
    for string in strings:
        if needle.upper() in string.upper():
            print(string)
else:
    print('Ошибка ввода')
