numbers = int(input('Введите число равное 2 или больше: '))
max = 0

for i in range(1, numbers + 1):
    user_number = int(input('Введите число: '))
    if user_number > max:
        max = user_number

print(max)