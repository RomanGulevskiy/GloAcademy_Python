import random

class FileProvider:
    def get(self, path):
        file = open(path, 'r')
        data = file.read()
        file.close()
        return data
    
    def add(self, path, data):
        file = open(path, 'a')
        file.write(data)
        file.close()

class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer        

class QuestionsStorage:
    def get_all(self):
        questions = [
            Question('Сколько будет два плюс два умноженное на два?', 6),
            Question('Бревно нужно распилить на 10 частей, скольо надо сделать распилов?', 9),
            Question('На двух руках 10 пальцев. Сколько пальцев на 5 руках?', 25),
            Question('Укол делают каждые полчаса, сколько нужно минут для трех уколов?', 60),
            Question('Пять свечей горело, две потухли. Сколько свечей осталось?', 2)
        ]

        return questions

class User:
    def __init__(self, name, right_answers=0, title=''):
        self.name = name
        self.right_answers = right_answers
        self.title = title

    def accept_right_answer(self):
        self.right_answers += 1

class UsersResultStorage:
    def save(self, user):
        file = 'results.txt'
        data = f'{user.name}\{user.right_answers}\{user.title}\n'
        file_provider = FileProvider()
        file_provider.add(file, data)

    def get_all(self):
        file = 'results.txt'
        file_provider = FileProvider()
        data = file_provider.get(file).strip('\n')
        data = data.split('\n')
        users = []

        for line in data:
            values = line.split('\\')
            user = User(values[0], values[1], values[2])
            users.append(user)
            
        return users

def show_user_results():
    name = 'Имя'
    points = 'Правильные ответы'
    title = 'Звание'
    print(f'{name:15}{points:25}{title:15}')

    results = UsersResultStorage().get_all()
    
    for result in results:
        print(f'{result.name:15}{result.right_answers:25}{result.title:15}')

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

questions_storage = QuestionsStorage()
users_result_storage = UsersResultStorage()

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
        user_answer = input()
        
        while not user_answer.isdigit():
            print('Введите число!')
            user_answer = input()
            
        if int(user_answer) == questions[random_index].answer:
            user.accept_right_answer()
        
        questions.pop(random_index)
        print()

    print('Количество правильных ответов: ', user.right_answers, '.', sep='')
    user.title = get_title(user.right_answers, number_of_questions)
    print('Поздравляем! ', user.name, ', вы - ', user.title, '!', sep='', end='\n\n')

    users_result_storage.save(user)
    
    play_again = input('Хотите сыграть еще раз? Да/Нет/Результаты: ')

    if play_again.upper() == 'ДА':
        play()
    elif play_again.upper() == 'РЕЗУЛЬТАТЫ':
        show_user_results()
    else:
        return

print('Добро пожаловать в программу тестирования My-Tester!')
print('Вам будет предложено ответить на несколько вопросов.', end='\n\n')
play()
