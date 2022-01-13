# -*- coding: utf-8 -*-

import random
import os
import jsonpickle


class FileProvider:
    def read(self, path):
        file = open(path, 'r', encoding='utf-8')
        data = file.read()
        file.close()
        return data

    def write(self, path, data):
        file = open(path, 'w', encoding='utf-8')
        file.write(data)
        file.close()

    def exists(self, path):
        return os.path.exists(path)


class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer        


class QuestionsStorage:
    def __init__(self):
        self.file = 'questions.json'

    def get_all(self):
        if file_provider.exists(self.file):
            data = file_provider.read(self.file)
            questions = jsonpickle.decode(data)
        else:
            questions = [
                Question('Сколько будет два плюс два умноженное на два?', 6),
                Question('Бревно нужно распилить на 10 частей, скольо надо сделать распилов?', 9),
                Question('На двух руках 10 пальцев. Сколько пальцев на 5 руках?', 25),
                Question('Укол делают каждые полчаса, сколько нужно минут для трех уколов?', 60),
                Question('Пять свечей горело, две потухли. Сколько свечей осталось?', 2)
            ]

            self.save_questions(questions)

        return questions

    def save_questions(self, questions):
        json_data = jsonpickle.encode(questions)
        file_provider.write(self.file, json_data)


class User:
    def __init__(self, name, right_answers=0, title=''):
        self.name = name
        self.right_answers = right_answers
        self.title = title

    def accept_right_answer(self):
        self.right_answers += 1


class UsersResultStorage:
    def __init__(self):
        self.file = 'results.json'

    def get_all(self):
        if file_provider.exists(self.file):
            data = file_provider.read(self.file)
            results = jsonpickle.decode(data)
        else:
            results = []

        return results

    def save_results(self, result):
        results = self.get_all()
        results.append(result)
        json_data = jsonpickle.encode(results)
        file_provider.write(self.file, json_data)


def show_user_results():
    name = 'Имя'
    points = 'Баллов'
    title = 'Звание'
    print(f'{name:15}{points:^10}{title:^15}')

    results = UsersResultStorage().get_all()
    
    for result in results:
        print(f'{result.name:15}{result.right_answers:^10}{result.title:^15}')


def get_title(points, questions):
    right_answers_percent = points / questions * 100

    if right_answers_percent == 100:
        return 'гений'
    elif right_answers_percent >= 80 and right_answers_percent < 100:
        return 'талант'
    elif right_answers_percent >= 50 and right_answers_percent < 80:
        return 'нормальный'
    elif right_answers_percent >= 20 and right_answers_percent < 50:
        return 'дурак'
    elif right_answers_percent > 0 and right_answers_percent < 20:
        return 'кретин'
    elif points == 0:
        return 'идиот'


def get_user_answer():
    user_input = input()

    while not user_input.isdigit():
        print('Ошибка ввода! Введите число!')
        user_input = input()

    return int(user_input)


def print_questions(questions):
    for i in range(len(questions)):
        print(f'Вопрос №{i+1}', questions[i].text, questions[i].answer)


def add_question():
    questions = questions_storage.get_all()

    print('Введите текст вопроса: ')
    text = input()
    print('Введите ответ: ')
    answer = get_user_answer()

    question = Question(text, answer)
    questions.append(question)
    questions_storage.save_questions(questions)


def remove_question():
    questions = questions_storage.get_all()
    while True:
        print('Введите номер вопроса, который хотите удалить: ')

        print_questions(questions)

        user_input = get_user_answer()
        if user_input < 1 and user_input > len(questions):
            print('Такого вопроса не существует!')
            continue

        questions.pop(user_input - 1)
        questions_storage.save_questions(questions)
        print(f'Вопрос №{user_input} успешно удален!')
        break


questions_storage = QuestionsStorage()
users_result_storage = UsersResultStorage()
file_provider = FileProvider()
jsonpickle.set_encoder_options('json', indent=4, separators=(',', ': '), ensure_ascii=False)

def play():
    user_name = input('Как к вам можно обращаться? ')
    user = User(user_name)
    print()

    questions = questions_storage.get_all()
    number_of_questions = len(questions)

    for i in range(len(questions)):
        random_index = random.randint(0, len(questions) - 1)

        print(f'Вопрос №{i+1}')
        print(questions[random_index].text)
        user_answer = get_user_answer()

        if user_answer == int(questions[random_index].answer):
            user.accept_right_answer()

        questions.pop(random_index)
        print()

    print('Количество правильных ответов: ', user.right_answers, '.', sep='')
    user.title = get_title(user.right_answers, number_of_questions)
    print('Поздравляем! ', user.name, ', вы - ', user.title, '!', sep='', end='\n\n')

    users_result_storage.save_results(user)
    
    user_choice = input('Хотите посмотреть все результаты? Введите "ДА" или "НЕТ": ')
    if user_choice.upper() == 'ДА':
        show_user_results()

    user_choice = input('Хотите пройти тест еще раз? Введите "ДА" или "НЕТ": ')
    if user_choice.upper() == 'ДА':
        play()

    user_choice = input('Хотите добавить новый вопрос? Введите "ДА" или "НЕТ": ')
    if user_choice.upper() == 'ДА':
        add_question()

    user_choice = input('Хотите удалить вопрос? Введите "ДА" или "НЕТ": ')
    if user_choice.upper() == 'ДА':
        remove_question()


print('Добро пожаловать в программу тестирования My-Tester!')
print('Вам будет предложено ответить на несколько вопросов.', end='\n\n')
play()
