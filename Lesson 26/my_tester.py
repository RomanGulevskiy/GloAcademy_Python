# -*- coding: utf-8 -*-

import random
import sqlite3


class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer        


class QuestionsStorage:
    def __init__(self, connection):
        self.connection = connection

        cursor = connection.cursor()

        cursor.execute(''' SELECT count(*) FROM sqlite_master WHERE type='table' AND name='questions' ''')

        if cursor.fetchone()[0] == 0:
            cursor.execute("""CREATE TABLE questions(
            Text TEXT PRIMARY KEY,
            Answer INTEGER);""")
            connection.commit()

            questions = [
                Question('Сколько будет два плюс два умноженное на два?', 6),
                Question('Бревно нужно распилить на 10 частей, скольо надо сделать распилов?', 9),
                Question('На двух руках 10 пальцев. Сколько пальцев на 5 руках?', 25),
                Question('Укол делают каждые полчаса, сколько нужно минут для трех уколов?', 60),
                Question('Пять свечей горело, две потухли. Сколько свечей осталось?', 2)
            ]

            self.save_questions(questions)

    def get_all(self):
        cursor = self.connection.cursor()
        cursor.execute('SELECT * FROM questions')
        rows = cursor.fetchall()
        questions = []

        for row in rows:
            question = Question(row[0], row[1])
            questions.append(question)

        return questions

    def save_questions(self, questions):
        for question in questions:
            self.insert_question(question)

    def insert_question(self, question):
        query = f"""INSERT INTO questions (Text, Answer) VALUES ('{question.text}', '{question.answer}')"""
        cursor = self.connection.cursor()
        cursor.execute(query)
        self.connection.commit()

    def delete_question(self, index):
        questions = self.get_all()
        question_to_delete = questions.pop(index)
        query = f"""DELETE FROM questions WHERE Text = '{question_to_delete.text}';"""
        cursor = self.connection.cursor()
        cursor.execute(query)
        self.connection.commit()


class User:
    def __init__(self, name, right_answers=0, title=''):
        self.name = name
        self.right_answers = right_answers
        self.title = title

    def accept_right_answer(self):
        self.right_answers += 1


class UsersResultStorage:
    def __init__(self, connection):
        self.connection = connection
        self.file = 'results.json'

        cursor = connection.cursor()

        cursor.execute(''' SELECT count(*) FROM sqlite_master WHERE type='table' AND name='results' ''')

        if cursor.fetchone()[0] == 0:
            cursor.execute("""CREATE TABLE results(
            id INTEGER PRIMARY KEY,
            user TEXT,
            points INTEGER,
            title TEXT);""")
            connection.commit()

    def get_all(self):
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM results;')
        rows = cursor.fetchall()
        results = []

        for row in rows:
            user = User(row[1], row[2], row[3])
            results.append(user)

        return results

    def save_result(self, result):
        query = f"""INSERT INTO results (user, points, title) VALUES ('{result.name}', '{result.right_answers}', '{result.title}')"""
        cursor = self.connection.cursor()
        cursor.execute(query)
        self.connection.commit()


def show_user_results():
    name = 'Имя'
    points = 'Баллов'
    title = 'Звание'
    print(f'{name:15}{points:^10}{title:^15}')

    results = UsersResultStorage(connection).get_all()
    
    for result in results:
        print(f'{result.name:15}{result.right_answers:^10}{result.title:^15}')


def get_title(points, questions):
    right_answers_percent = points / questions * 100

    if right_answers_percent == 100:
        return 'гений'
    elif 80 <= right_answers_percent < 100:
        return 'талант'
    elif 50 <= right_answers_percent < 80:
        return 'нормальный'
    elif 20 <= right_answers_percent < 50:
        return 'дурак'
    elif 0 < right_answers_percent < 20:
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
    print('Введите текст вопроса: ')
    text = input()
    print('Введите ответ: ')
    answer = get_user_answer()

    question = Question(text, answer)
    questions_storage.insert_question(question)


def remove_question():
    questions = questions_storage.get_all()
    while True:
        print('Введите номер вопроса, который хотите удалить: ')

        print_questions(questions)

        user_input = get_user_answer()
        if 1 > user_input > len(questions):
            print('Такого вопроса не существует!')
            continue

        questions_storage.delete_question(user_input - 1)
        print(f'Вопрос №{user_input} успешно удален!')
        break


connection = sqlite3.connect('my_tester.db')
questions_storage = QuestionsStorage(connection)
users_result_storage = UsersResultStorage(connection)


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

    users_result_storage.save_result(user)
    
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
