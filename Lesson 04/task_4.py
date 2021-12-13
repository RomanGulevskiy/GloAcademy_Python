r = int(input())
k = int(input())
n = int(input())
print('За', n, 'мячей нужно заплатить', r * n + k * n // 100, 'рублей', k * n % 100, 'копеек')