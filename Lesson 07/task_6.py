num = int(input('Введите число: '))
total = 0

for i in range(1, num + 1):
    if i % 10 == 1 or i % 10 == 3 or i % 10 == 7:
        total += i
    
print(total)
