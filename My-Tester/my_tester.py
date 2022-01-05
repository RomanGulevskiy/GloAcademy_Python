import random

def get_title(points):
    if points == 5:
        return 'гений'
    elif points == 4:
        return 'талант'
    elif points == 3:
        return 'нормальный'
    elif points == 2:
        return 'урак'
    elif points == 1:
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
        
        print('Вопрос №', i + 1, sep='')
        user_answer = int(input(questions[random_index] + ': '))

        if user_answer == answers[random_index]:
            right_answers_counter += 1
        
        questions.pop(random_index)
        answers.pop(random_index)

    print()
    print('Количество правильных ответов: ', right_answers_counter, '.', sep='')
    title = get_title(right_answers_counter)
    print('Поздравляем! ', user_name, ', вы - ', title, '!', sep='')
    print()
    
    play_again = input('Хотите сыграть еще раз? Да/Нет: ')

    if play_again.upper() == 'ДА':
        play()
    else:
        return

print('Добро пожаловать в программу тестирования My-Tester!')
print('Вам будет предложено ответить на несколько вопросов.', end='\n\n')
play()