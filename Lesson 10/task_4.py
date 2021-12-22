c = input('Введите символ: ')

if ord(c) >= 65 and ord(c) <= 90:
    print(c.lower())
elif ord(c) >= 97 and ord(c) <= 122:
    print(c.upper())
else:
    print(c)
    