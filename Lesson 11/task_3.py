ip_address = input('Введите ip-адрес: ').split('.')

if len(ip_address) == 4:
    flag = 1
    for partial_ip_address in ip_address:
        if int(partial_ip_address) not in range(0, 256):
            flag = 0
            break
    if flag == 1:
        print('YES')
    else:
        print('NO')
else:
    print('Ошибка ввода')
