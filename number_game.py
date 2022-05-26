from random import *

def is_valid(number, lim):
    if number.isdigit() == True:
        number = int(number)
        if 1 <= number <= lim:
            return True
        else:
            return False
    else:
        return False


def rand_om(lim):
    num = randrange(1, lim + 1)
    return num
    


answer = ''
print('Добро пожаловать в числовую угадайку')

while answer.lower() != 'н':
    print('Задайте сложность игры от 1 до 100')
    difficulty = input()
    lim = 100
    if is_valid(difficulty, lim) == True:
        difficulty = int(difficulty)
        p = rand_om(difficulty)
        print('Попробуйте угадать ваше число от 1 до', difficulty)

        s = 0
        n = '0'

        while n != p:
            n = input()
            if is_valid(n, difficulty) == True:
                n = int(n)
                s += 1
                if n < p:
                    print('Слишком мало, попробуйте еще раз')
                    continue
                elif n > p:
                    print('Слишком много, попробуйте еще раз')
                    continue
                else:
                    break            
            else:
                print('А может быть все-таки введем целое число от 1 до', difficulty, '?')
                continue
    else:
        print('А может быть все-таки введем целое число от 1 до', lim, '?')
        continue
    print('Вы угадали ваше число', p, 'c', s, 'попыток, поздравляем!')
    print('Сыграем еще раз?','Нажите "д" - еще раз, или "н" - конец игры.')
    answer = input()
print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
