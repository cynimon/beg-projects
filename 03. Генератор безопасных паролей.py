import random
digits = '0123456789'
lowercase = 'abcdefghijklmnopqrstuvwxyz'
uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
symb = '!#$%&*+-=?@^_'
nones = 'il1Lo0O'
chars = ''

# выбор состава пароля
def include(yn):
    if yn == 'д':
        return True
    else:
        return False

# генерация всех символов в строке char
def char_getting(chars, digf, upperf, lowerf, symbf, nonesf):
    if symbf == True:
            chars += symb
    if nonesf == False:
        if digf == True:
            chars += digits
        if upperf == True:
            chars += uppercase
        if lowerf == True:
            chars += lowercase
# без неоднозначных символов
    if nonesf == True:
        if digf == True:
            for c in digits:
                if c not in '10':
                    chars += c
        if upperf == True:
            for c in uppercase:
                if c not in nones:
                    chars += c
        if lowerf == True:
            for c in lowercase:
                if c not in nones:
                    chars += c
    return chars

# генерация пароля
def gen_password(length, chars):
    return random.sample(chars, length)

# параметры паролей
print('Сколько паролей необходимо?')
n = int(input())
print('Длина пароля?')
length = int(input())
print('Включать ли цифры', digits, '?', 'Д/Н')
digf = include(input())
print('Включать ли прописные буквы', uppercase, '?', 'Д/Н')
upperf = include(input())
print('Включать ли строчные буквы', lowercase, '?', 'Д/Н')
lowerf = include(input())
print('Включать ли символы', symb, '?', 'Д/Н')
symbf = include(input())
print('Исключать ли неоднозначные символы', nones, '?', 'Д/Н')
nonesf = include(input())

# получение возоможных символов и генерация паролей
chars = char_getting(chars, digf, upperf, lowerf, symbf, nonesf)
for _ in range(n):
    print(*gen_password(length, chars), sep='')


