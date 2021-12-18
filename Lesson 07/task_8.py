numbers = int(input('Введите число равное 2 или больше: '))
min = 0
max = 0

for i in range(numbers + 1):
    user_number = int(input('Введите число: '))
    if i == 0:
        min = user_number
        max = user_number
    if user_number > max:
        max = user_number
    elif user_number < min:
        min = user_number

print('Минимум равен', min)
print('Максимум равен', max)