import random

def save_result(result):
    file = open('results.txt', 'a')
    file.write(result)
    file.close()

def get_results():
    name = 'Имя'
    points = 'Правильные ответы'
    title = 'Звание'
    print(f'{name:15}{points:25}{title:15}')
    file = open('results.txt', 'r')
    line = file.readline()
    while line:
        line = line.split('\\')
        name = line[0]
        points = line[1]
        title = line[2].strip('\n')
        print(f'{name:15}{points:25}{title:15}')
        line = file.readline()

    file.close()

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

def play():
    user_name = input('Как к вам можно обращаться? ')
    print()
    
    questions = [
        'Сколько будет два плюс два умноженное на два?',
        'Бревно нужно распилить на 10 частей, скольо надо сделать распилов?',
        'На двух руках 10 пальцев. Сколько пальцев на 5 руках?',
        'Укол делают каждые полчаса, сколько нужно минут для трех уколов?',
        'Пять свечей горело, две потухли. Сколько свечей осталось?'
    ]
    
    answers = [6, 9, 25, 60, 2]

    right_answers_counter = 0
    
    number_of_questions = len(questions)
    
    for i in range(number_of_questions):
        random_index = random.randint(0, len(questions) - 1)
        
        print(f'Вопрос №{i+1}')
        print(questions[random_index])
        user_answer = input()
        
        while not user_answer.isdigit():
            print('Введите число!')
            user_answer = input()
            
        if int(user_answer) == answers[random_index]:
            right_answers_counter += 1
        
        questions.pop(random_index)
        answers.pop(random_index)
        print()

    print('Количество правильных ответов: ', right_answers_counter, '.', sep='')
    title = get_title(right_answers_counter, number_of_questions)
    print('Поздравляем! ', user_name, ', вы - ', title, '!', sep='', end='\n\n')

    result = f'{user_name}\{right_answers_counter}\{title}\n'
    save_result(result)
    
    play_again = input('Хотите сыграть еще раз? Да/Нет/Результаты: ')

    if play_again.upper() == 'ДА':
        play()
    elif play_again.upper() == 'РЕЗУЛЬТАТЫ':
        get_results()
    else:
        return

print('Добро пожаловать в программу тестирования My-Tester!')
print('Вам будет предложено ответить на несколько вопросов.', end='\n\n')
play()
