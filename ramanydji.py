n = int(input('Введите ограничение диапазона для нахождения чисел Рамануджана:'))

total = 0

for a in range(1, n):

    for b in range(1, n):

        for c in range(1, n):

            for d in range(1, n):

                if a ** 3 + b ** 3 == c ** 3 + d ** 3 and a != d and b != c and b != d and a > b and c > d and a > c:

                    c, d = a, b

                    total += 1

                    print('a =', a, 'b =', b, 'c =', c, 'd=', d, '=', a ** 3 + b ** 3 )

print('Общее количество натуральных решений =', total)


   
                        
