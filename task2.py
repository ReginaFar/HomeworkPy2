# 2) Для списка реализовать обмен значений соседних элементов, т.е. значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

elements_quantity = int(input('Введите количество элементов списка:'))
my_list = []
element = 0
for i in range(elements_quantity):
    my_list.append(input('Введите значение списка:'))
print(my_list)

for el in range(int(len(my_list)/2)):
    my_list[element], my_list[element +
                              1] = my_list[element + 1], my_list[element]
    element += 2
print(my_list)
