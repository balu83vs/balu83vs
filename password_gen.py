from random import *

# initialisation
def initialisation():

    digits = ''
    for i in range(10):
        digits += str(i)

    lowercase_letters = ''
    for i in range(97, 123):
        lowercase_letters += chr(i)   

    uppercase_letters = lowercase_letters.upper()

    punctuation = '!#$%&*+-=?@^_'
    
    return digits, lowercase_letters, uppercase_letters, punctuation

# generation
def generate_pass(len_pass, digit_pass, uppercase_pass, lowercase_pass, punct_pass):
    chars = ''

    digits, lowercase_letters, uppercase_letters, punctuation = initialisation()
    
    if digit_pass == True:
        chars = digits
    if uppercase_pass == True:
        chars += uppercase_letters
    if lowercase_pass == True:
        chars += lowercase_letters
    if punct_pass == True:
        chars += punctuation

    password = sample(chars, len_pass)

    
   # randint()
   # randrange()
   # choice()
   # sample()
     
     
    return password



#qustions
digits, lowercase_letters, uppercase_letters, punctuation = initialisation()

print('Сколько паролей сгенерировать?')
num_pass = int(input())

print('Какая длина пароля Вам нужна?')
len_pass = int(input())

print('Пароль содержит', digits, '?, Д/Н')
if input().lower() == 'д':
    digit_pass = True
else:
    digit_pass = False

print('Пароль содержит', uppercase_letters, '?, Д/Н')
if input().lower() == 'д':
    uppercase_pass = True
else:
    uppercase_pass = False

print('Пароль содержит', lowercase_letters, '?, Д/Н')
if input().lower() == 'д':
    lowercase_pass = True
else:
    lowercase_pass = False

print('Пароль содержит', punctuation, '?, Д/Н')
if input().lower() == 'д':
    punct_pass = True
else:
    punct_pass = False    

# exit
for i in range(num_pass):
    print('Ваш пароль №', i+1, ':', *generate_pass(len_pass, digit_pass, uppercase_pass, lowercase_pass, punct_pass))
