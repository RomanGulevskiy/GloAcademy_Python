num = int(input('Введите число: '))
total = 0
counter = 0

while num != 0:
    total += num
    counter += 1
    num = int(input('Введите число: '))

print(total / counter)
