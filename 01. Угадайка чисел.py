import random

# сравнение чисел
def check_input(x, y):
    if y < x:
        print('Слишком мало, попробуйте еще раз')
        return False
    elif y > x:
        print('Слишком много, попробуйте еще раз')
        return False
    elif y == x:
        print('Вы угадали, поздравляем!')
        return True

# валидность ввода
def is_okay(y, n):
    if y.isdigit():
        if int(y) in range(1, int(n) + 1):
            return False
        else:
            print(f'А может быть все-таки введем целое число от 1 до {n}?')
            return True
    else:
        print(f'А может быть все-таки введем целое число от 1 до {n}?')
        return True

# проверка корректности вводимой границы
def check_n(n):
    if n.isdigit():
        return n
    else:
        print('Упс! Принимаются только целые числа.')
        restart_input()

# ввод числа y пользователем
def main_game():
    print('Укажите верхнюю границу числа:')
    n = input()
    check_n(n)
    x = random.randint(1, int(n))
    nice = False
    counter = 0
    print('Введите число:')
    while nice == False:
        y = input()
        if is_okay(y, n):
            continue
        else:
            y = int(y)
            nice = check_input(x, y)
        counter += 1
    print('Количество попыток:', counter)
    print('Введите "д", чтобы сыграть ещё, введите "н", чтобы закрыть игру')
    restart_game()

# ввод границы заново
def restart_input():
    main_game()

# рестарт игры
def restart_game():
    answ = input()
    if answ == 'д':
        main_game()
    elif answ == 'н':
        print('Спасибо, что играли в числовую угадайку. Увидимся!')

# начало игры
print('Добро пожаловать в числовую угадайку')
main_game()


