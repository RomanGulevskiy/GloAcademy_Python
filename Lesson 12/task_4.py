def calc_delivery_price(amount):
    if amount == 1:
        return 100
    else:
        return amount * 50 + 50

amount = int(input('Введите количество товаров в заказе: '))
if amount > 0:
    print(calc_delivery_price(amount))
else:
    print('Ошибка ввода')