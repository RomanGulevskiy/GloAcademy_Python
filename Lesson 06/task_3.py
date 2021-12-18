str1 = input('Введите текст: ')
str2 = input('Введите текст: ')
str3 = input('Введите текст: ')

if len(str1) >= len(str2) and len(str1) >= len(str3):
    print(str1)
elif len(str2) >= len(str1) and len(str2) >= len(str3):
    print(str2)
else:
    print(str3)
