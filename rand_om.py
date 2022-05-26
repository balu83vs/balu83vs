from random import *

def rand_om():
    num = randrange(1, 101)
    print('Добро пожаловать в числовую угадайку')
    return num
    
def is_valid(n):
    if n.isdigit() == True:
        n = int(n)
        if 1 <= n <= 100:
            return True
        else:
            return False
    else:
        return False
   
p = rand_om()
print('Попробуйте угадать ваше число от 1 до 100')

s = 0
n = '0'


while n != p:
    n = input()
    if is_valid(n) == True:
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
        print('А может быть все-таки введем целое число от 1 до 100?')
        continue

print('Вы угадали ваше число', p, 'c', s, 'попыток, поздравляем!')
