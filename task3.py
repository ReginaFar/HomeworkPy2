# 3) Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

seasons_list = ['winter', 'spring', 'summer', 'autumn']
seasons_dict = {1: 'winter', 2: 'spring', 3: 'summer', 4: 'autumn'}
number_month = int(input('Введите номер месяца:'))
if number_month == 12 or number_month == 1 or number_month == 2:
    print(seasons_list[0])
    print(seasons_dict.get(1))
elif number_month > 2 and number_month < 6:
    print(seasons_list[1])
    print(seasons_dict.get(2))
elif number_month > 5 and number_month < 9:
    print(seasons_list[2])
    print(seasons_dict.get(3))
elif number_month > 8 and number_month < 12:
    print(seasons_list[3])
    print(seasons_dict.get(4))
else:
    print('Это не номер месяца')
