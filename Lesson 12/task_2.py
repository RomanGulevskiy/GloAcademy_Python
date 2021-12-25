def find_max_list_element(numbers):
    numbers = numbers.split()
    numbers = list(map(int, numbers))
    return max(numbers)
    
numbers_1 = input('Введите список натуральных чисел, разделенных пробелом: ')
numbers_2 = input('Введите список натуральных чисел, разделенных пробелом: ')
max_number_1 = find_max_list_element(numbers_1)
max_number_2 = find_max_list_element(numbers_2)
print(max_number_1 * max_number_2)
