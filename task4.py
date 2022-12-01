# 4) Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки.
# Строки необходимо пронумеровать.
# Если слово длинное, выводить только первые 10 букв в слове.

my_string = input('Введите предложение:').split()
number = 1
for i in range(len(my_string)):
    if len(my_string[i]) > 10:
        print(number, my_string[i][0:10])
        number += 1
    else:
        print(number, my_string[i])
        number += 1
