import random

word_list = [
    "тысяча",
    "книга",
    "возможность",
    "результат",
    "ночь",
    "стол",
    "имя",
    "область",
    "статья",
    "число",
    "компания",
    "народ",
    "жена",
    "группа",
    "развитие",
    "процесс",
    "суд",
    "условие",
    "средство",
    "начало",
    "свет",
    "пора",
    "путь",
    "душа",
    "уровень",
    "форма",
    "связь",
    "минута",
    "улица",
    "вечер",
    "качество",
    "мысль",
    "дорога",
    "мать",
    "действие",
    "месяц",
    "государство",
    "кровь",
    "район",
    "небо",
    "армия",
    "класс",
    "представитель",
    "участие",
    "девочка",
    "политика",
    "герой",
    "картина",
    "доллар",
    "спина",
    "территория",
    "пол",
    "поле",
    "изменение",
    "направление",
    "рисунок",
    "течение",
    "церковь",
    "банк",
    "сцена",
    "население",
    "большинство",
    "музыка",
    "правда",
    "свобода",
    "память",
    "команда",
    "союз",
    "врач",
    "договор",
    "дерево",
    "факт",
    "хозяин",
    "природа",
    "угол",
    "телефон",
    "позиция",
    "двор",
    "писатель",
    "самолет",
    "объем",
    "род",
    "солнце",
    "вера",
    "берег",
    "спектакль",
    "фирма",
    "способ",
    "завод",
    "цвет",
    "журнал",
    "руководитель",
    "специалист",
    "оценка",
    "регион",
    "песня",
    "процент",
    "родитель",
    "море",
    "требование",
    "основание",
    "половина",
    "роман",
    "круг",
    "анализ",
    "стихи",
    "автомобиль",
    "экономика",
    "литература",
    "бумага",
    "поэт",
]


def get_word():
    return random.choice(word_list).upper()

def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                # голова, торс, обе руки, одна нога
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     /
                   -
                ''',
                # голова, торс, обе руки
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |
                   -
                ''',
                # голова, торс и одна рука
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |
                   -
                ''',
                # голова и торс
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |
                   -
                ''',
                # голова
                '''
                   --------
                   |      |
                   |      O
                   |
                   |
                   |
                   -
                ''',
                # начальное состояние
                '''
                   --------
                   |      |
                   |
                   |
                   |
                   |
                   -
                '''
    ]
    return stages[tries]

def play(word):
    word_completion = '_' * len(word)  # строка, содержащая символы _ на каждую букву задуманного слова
    guessed = False                    # сигнальная метка
    guessed_letters = []               # список уже названных букв
    guessed_words = []                 # список уже названных слов
    tries = 6
    print('Давайте играть в угадайку слов!')
    print(display_hangman(tries))
    print(word_completion)
    print('Привет! Введи букву или слово на русском:')
    while guessed == False:
        a = input()
        count = 0
        for c in a:
            if c.isalpha() == False:
                count += 1
        if count != 0:
            print('Введите слово из букв')
            continue
        # ввод одной буквы
        if len(a) == 1:
            if a.upper() in guessed_letters:
                print('Такая буква уже была')
                continue
            else:
                guessed_letters.append(a.upper())
            if a.upper() in word.upper():
                # замена прочерков в выводе на нужную букву
                for i in range(len(word)):
                    word_completion = list(word_completion)
                    if word[i].upper() == a.upper():
                        word_completion[i] = a
                word_completion = ''.join(word_completion)
                print(word_completion)
            if a.upper() not in word.upper():
                tries -= 1
                print(display_hangman(tries))
                print(word_completion)
        # проверки при вводе слова, а не буквы
        elif len(a) > 1:
            if a.upper() in guessed_words:
                print('Такое слово уже было')
                continue
            else:
                guessed_words.append(a.upper())
            if a.upper() == word.upper():
                print('Поздравляем, вы угадали слово! Вы победили!')
                guessed = True
            else:
                tries -= 1
                print(display_hangman(tries))
                print(word_completion)
        # проверка флага для цикла
        if guessed == False and tries == 0:
            print(word)
            print('Вы проиграли')
            print('Сыграть ещё раз? Да = 1, нет = 2')
            answ = int(input())
            return answ
        elif word_completion.upper() == word.upper():
            guessed = True
            print('Поздравляем! Вы угадали слово! Вы победили')
    print('Сыграть ещё раз? Да = 1, нет = 2')
    answ = int(input())
    return answ

answ = 1
while answ == 1:
    word = get_word()
    answ = play(word)
