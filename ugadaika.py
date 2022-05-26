from random import *

mylist = ['занавеска', 'лист', 'трактор', 'стеллаж', 'одуванчик', 'мама', 'свобода', 'скамейка', 'приложение', 'дом']

# функция получения текущего состояния
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

# выдача слова
def get_word(mylist):
    word = mylist[randrange(10)].upper()
    return word


# основная механика
def play(word):
    word_completion = []               # строка, содержащая символы _ на каждую букву задуманного слова
    guessed_letters = []               # список уже названных букв
    guessed_word = []                  # слово
    guessed_words = []                 # список уже названных слов
    tries = 6                          # количество попыток
    print('Давайте играть в угадайку слов!')
    
    guessed_word = [c for c in word]

    word_completion = ['_' for i in range(len(guessed_word))]
    print(*word_completion) 
    
    while tries > 0 and word_completion.count('_') != 0:
        print(display_hangman(tries))
        print('Введите букву:')
        letter = input()
        count = guessed_word.count(letter.upper())
        if letter not in guessed_letters:
            guessed_letters.append(letter)
            for i in range(len(guessed_word)):
                if letter.upper() == guessed_word[i]:                  
                    word_completion[i] = letter
                    count -= 1
                    if count == 0:
                        print('')
                        print('Отлично, открываем угаданную букву!')
                        print('')
                        print(*word_completion)
                elif guessed_word.count(letter.upper()) == 0:
                    print('')
                    print('Такой буквы нет! Попробуй еще.')
                    print('')
                    print(*word_completion)
                    tries -= 1
                    break                           
        else:
            print('')
            print('Такую букву Вы уже называли! Попробуйте ввести другую')
            print('')
            print(*word_completion)
            
    if word_completion.count('_') == 0:
        print(display_hangman(tries))
        print('')
        print('Вы победили!!!')
    else:
        print(display_hangman(tries))
        print('')
        print('Вы не угадали слово!')

ans = ''
while ans != 'Н':
    play(get_word(mylist))
    print('Хотите продолжить? Д/Н')
    ans = input().upper()

    

