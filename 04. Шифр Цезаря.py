output = ''

print('Направление шифра? Шифрование - 1, дешифрование - 2')
direction = int(input())
print('Язык алфавита? Русский - 1, английский - 2')
lang = int(input())
print('Шаг сдвига (введите цифру)')
step = int(input())
print('Введите текст:')
needed = input()

# шифрование
def shifr(x, step, lang):
    y = ''
    for c in x:
        if lang == 1:
            if 1040 <= ord(c) + step <= 1071:
                y += chr((ord(c) + step))
            elif 1072 <= ord(c) + step <= 1103:
                y += chr((ord(c) + step))
            elif ord(c) + step > 1071 or ord(c) + step > 1103:
                y += chr((ord(c) + step - 32))
            elif ord(c) in [32, 44, 46, 33, 63]:
                y += c
        if lang == 2:
            if 97 <= ord(c) + step <= 122:
                y += chr((ord(c) + step))
            elif 65 <= ord(c) + step <= 90:
                y += chr((ord(c) + step))
            elif ord(c) + step > 122 or ord(c) + step > 90:
                y += chr((ord(c) + step - 26))
            elif ord(c) in [32, 44, 46, 33, 63]:
                y += c
    return y

# дешифрование
def deshifr(x, step, lang):
    y = ''
    for c in x:
        if lang == 1:
            if 1040 <= ord(c) - step <= 1071:
                y += chr((ord(c) - step))
            elif 1072 <= ord(c) - step <= 1103:
                y += chr((ord(c) - step))
            elif ord(c) - step < 1040 or ord(c) - step < 1072:
                y += chr((ord(c) - step + 32))
            elif ord(c) == 32:
                y += ' '
        if lang == 2:
            if 97 <= ord(c) - step <= 122:
                y += chr((ord(c) - step))
            elif 65 <= ord(c) - step <= 90:
                y += chr((ord(c) - step))
            elif ord(c) - step < 97 or ord(c) - step < 65:
                y += chr((ord(c) - step + 26))
            elif ord(c) == 32:
                y += ' '
    return y

if direction == 1:
    output = shifr(needed, step, lang)
elif direction == 2:
    output = deshifr(needed, step, lang)

print(output)
