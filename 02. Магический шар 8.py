import random

answers = [
    "Бесспорно",
    "Предрешено",
    "Никаких сомнений",
    "Определённо да",
    "Можешь быть уверен в этом",
    "Мне кажется - да",
    "Вероятнее всего",
    "Хорошие перспективы",
    "Знаки говорят - да",
    "Да",
    "Пока неясно, попробуй снова",
    "Спроси позже",
    "Лучше не рассказывать",
    "Сейчас нельзя предсказать",
    "Сконцентрируйся и спроси опять",
    "Даже не думай",
    "Мой ответ - нет",
    "По моим данным - нет",
    "Перспективы не очень хорошие",
    "Весьма сомнительно",
]

print('Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.')
print('Как тебя зовут?')
name = input()
print(f'Привет {name}')

flag = False

while flag == False:
    print(f'Введи свой вопрос, {name}')
    question = input()
    print(random.choice(answers))
    print('Есть ли у тебя ещё вопросы, путник? Да = "д", нет = "н"')
    question = input()
    if question == 'д':
        continue
    else:
        print('Возвращайся если возникнут вопросы!')
        flag = True

