# 3) Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

seasons_list = ['winter', 'spring', 'summer', 'autumn']
number_month = int(input('Введите номер месяца:'))
if number_month == 12 or number_month == 1 or number_month == 2:
    print(seasons_list[0])
elif number_month > 2 and number_month < 6:
    print(seasons_list[1])
elif number_month > 5 and number_month < 9:
    print(seasons_list[2])
elif number_month > 8 and number_month < 12:
    print(seasons_list[3])
else:
    print('Это не номер месяца')

seasons_dict = {'winter':  [12, 1, 2],
                'spring': [3, 4, 5],
                'summer':  [6, 7, 8],
                'autumn': [9, 10, 11]}

month_num = int(input('Введите номер месяца:'))
if month_num in range(1, 13):
    for i in seasons_dict.items():
        if month_num in i[1]:
            print(i[0])
            break
else:
    print('Это не номер месяца!')
