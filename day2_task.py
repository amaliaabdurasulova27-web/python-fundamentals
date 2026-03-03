# день2-3. Условия if/else

# num = int(input('Ведите число: '))
# if num % 2 == 0:
#     print('Это число четное')
# else:
#     print('Это число нечетное')




# num1 = int(input('Ведите число1: '))
# num2 = int(input('Ведите число2: '))
#
#
# if num1 > num2:
#     print(f'число {num1} больше чем {num2} ')
# elif num2 > num1:
#     print(f'число {num2} больше чем {num1} ')



# num1 = int(input("Введите число1: "))
# num2 = int(input("Введите число2: "))
# num3 = int(input("Введите число3: "))
#
# if num1 > num2 and num1 > num3:
#     print(f'Число {num1} самое наибольшее')
# elif num2 > num1 and num2 > num3:
#     print(f'Число {num2} самое наибольшее')
# else:
#     print(f'Число {num3} самое наибольшее')



# num = int(input('введите число: '))
#
# if num <= 0:
#     print(f'число {num} отрицательное')
# else:
#     print(f'число {num} положительное')



# num = int(input('Введите число: '))
#
# if num % 3 == 0:
#     print(f'Число делится на 3, ответ: {num / 3} ')
# else:
#     print('Число не делится на 3')


# num = int(input('Введите число: '))
#
# if num <= 10 or num <= 50:
#     print('Число в дипазоне')
# elif num <10:
#     print('Число меньше 10')
# elif num >50:
#     print('Число больше 50')



#консоль доступа по  возрасту
try:

    age = int(input('Введите свой возраст: '))

    if age < 0:
        print('Возраст не может быть отрицательным ')
    elif age == 0:
        print('Вы еще не родились')
    elif  0< age < 10:
        print('Доступ запрещен')
    elif 10 <= age <=17:
        print('Ограниченный доступ')
    elif 18 <= age <= 50:
        print('Полный доступ')
    elif 50 < age <= 100:
        print('Специальный режим')
    elif 0< age >100:
        print('Вы ввели не существующий возраст')

except ValueError:
    print('Можно вводить только числа')














