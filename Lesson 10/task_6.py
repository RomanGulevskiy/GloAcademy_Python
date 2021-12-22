s = input('Введите текст: ')

for c in range(len(s)):
    if s[c].isdigit():
        print(s[c], end='')
    