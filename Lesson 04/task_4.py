r = int(input())
k = int(input())
n = int(input())
print('За два мяча нужно заплатить', r * n + k * n // 100, 'рублей', k * n % 100, 'копеек')