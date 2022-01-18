import os
import jsonpickle


class FileProvider:
    def read(self, filepath):
        file = open(filepath, 'r', encoding='utf-8')
        data = file.read()
        file.close()
        return data

    def write(self, filepath, data):
        file = open(filepath, 'w', encoding='utf-8')
        file.write(data)
        file.close()

    def exists(self, filepath):
        return os.path.exists(filepath)


class School:
    def __init__(self, name='', address=''):
        self.filepath = 'school.json'
        self.name = name
        self.address = address

    def get_info(self):
        if file_provider.exists(self.filepath):
            data = file_provider.read(self.filepath)
            school = jsonpickle.decode(data)
        else:
            school = School()

        return school

    def save_info(self, school):
        json_data = jsonpickle.encode(school)
        file_provider.write(self.filepath, json_data)


class Student:
    def __init__(self, name, age, school_class):
        self.name = name
        self.age = age
        self.school_class = school_class


class StudentsStorage:
    def __init__(self):
        self.filepath = 'students.json'

    def get_all(self):
        if file_provider.exists(self.filepath):
            data = file_provider.read(self.filepath)
            students = jsonpickle.decode(data)
        else:
            students = []
            return students

        return students

    def save(self, students):
        json_data = jsonpickle.encode(students)
        file_provider.write(self.filepath, json_data)


def print_school_info():
    school = School().get_info()
    number_of_students = len(StudentsStorage().get_all())
    print()
    print(f'Название: {school.name}')
    print(f'Адрес: {school.address}')
    print(f'Количество учеников: {number_of_students}\n')


def edit_school_info():
    school = School()

    print()
    print('Введите название школы: ')
    school.name = get_user_answer('school_name')

    print('Введите адрес школы: ')
    school.address = get_user_answer('school_address')

    school.save_info(school)
    print('Данные успешно сохранены!\n')


def print_student_list():
    students = StudentsStorage().get_all()

    if len(students) == 0:
        print('Список учеников пуст.\n')
    else:
        number = '№'
        name = 'ФИО'
        age = 'Возраст'
        school_class = 'Класс'
        print()
        print(f'{number:<3}{name:25}{age:7}{school_class:>10}')
        for i in range(len(students)):
            name = students[i].name
            age = students[i].age
            school_class = students[i].school_class
            print(f'{i+1:<3}{name:25}{age:7}{school_class:>10}')

        print()


def remove_student():
    students = StudentsStorage().get_all()
    while True:
        print_student_list()
        print('Введите номер ученика, которого хотите удалить:')

        user_input = get_user_answer('student_number')
        if user_input < 0 or user_input > len(students):
            print('Такого ученика не существует.')
            continue

        students.pop(user_input - 1)
        StudentsStorage().save(students)
        print(f'Ученик №{user_input} успешно удален!\n')
        break


def add_student():
    students = StudentsStorage().get_all()

    print()
    print('Введите ФИО ученика: ')
    name = get_user_answer('name')

    print('Введите возраст ученика: ')
    age = get_user_answer('age')

    print('Введите класс ученика: ')
    school_class = get_user_answer('school_class')

    student = Student(name, age, school_class)
    students.append(student)

    StudentsStorage().save(students)
    print('Данные успешно сохранены!')
    print()


def get_user_answer(input_type):
    user_input = input()

    if input_type == 'name':
        error = 'error'
        while error != '':
            if len(user_input) == 0:
                error = 'Ошибка ввода! Поле не может быть пустым.'
                print(error)
                user_input = input()
                continue

            elif not user_input.isalpha():
                error = 'Ошибка ввода! ФИО не может содержать цифры.'
                print(error)
                user_input = input()
                continue

            else:
                return user_input

    elif input_type == 'age':
        error = 'error'
        while error != '':
            if len(user_input) == 0:
                error = 'Ошибка ввода! Поле не может быть пустым.'
                print(error)
                user_input = input()
                continue

            elif not user_input.lstrip('-').isdigit():
                error = 'Ошибка ввода! Значение поля должно быть числом.'
                print(error)
                user_input = input()
                continue

            elif int(user_input) < 0 or int(user_input) > 100:
                error = 'Ошибка ввода! Введен неверный возраст.'
                print(error)
                user_input = input()
                continue

            else:
                return int(user_input)

    elif input_type == 'student_number' or input_type == 'user_choice':
        error = 'error'
        while error != '':
            if len(user_input) == 0:
                error = 'Ошибка ввода! Поле не может быть пустым.'
                print(error)
                user_input = input()
                continue

            elif not user_input.lstrip('-').isdigit():
                error = 'Ошибка ввода! Значение поля должно быть числом.'
                print(error)
                user_input = input()
                continue

            else:
                return int(user_input)

    else:
        while len(user_input) == 0:
            print('Ошибка ввода! Поле не может быть пустым.')
            user_input = input()

        return user_input


file_provider = FileProvider()
jsonpickle.set_encoder_options('json', indent=4, separators=(',', ': '), ensure_ascii=False)


print('Добро пожаловать в программу управления онлайн-школой!')
print()
school = School().get_info()
while True:
    if school.name == '' and school.address == '':
        print('Введите название школы: ')
        school.name = get_user_answer('school_name')

        print('Введите адрес школы: ')
        school.address = get_user_answer('school_address')

        school.save_info(school)
        print('Данные успешно сохранены!')
        print()

    print('Выберите, что вы хотите сделать:')
    print('1 - Получить информацию о школе')
    print('2 - Изменить информацию о школе')
    print('3 - Посмотреть список учеников')
    print('4 - Добавить нового ученика')
    print('5 - Удалить ученика')
    print('6 - Выход')

    user_choice = get_user_answer('user_choice')

    while user_choice not in range(1, 7):
        print('Ошибка ввода! Такого пункта меню нет.')
        user_choice = get_user_answer('user_choice')

    if user_choice == 1:
        print_school_info()
    elif user_choice == 2:
        edit_school_info()
    elif user_choice == 3:
        print_student_list()
    elif user_choice == 4:
        add_student()
    elif user_choice == 5:
        remove_student()
    else:
        break
