# 6) *Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два элемента —
# номер товара и словарь с параметрами (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
# Пример готовой структуры:
# [
# (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
# (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
# (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]
# Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ —
# характеристика товара, например название, а значение — список значений-характеристик, например список названий товаров.
# Пример:
# {
# “название”: [“компьютер”, “принтер”, “сканер”],
# “цена”: [20000, 6000, 2000],
# “количество”: [5, 2, 7],
# “ед”: [“шт.”]
# }

goods = []
i = 1
while True:
    answer = input('Хотите добавить новый товар? Тогда введите "да": ')
    if answer.lower() != 'да':
        break
    goods_name = input("Название товара: ")
    goods_price = int(input("Цена товара: "))
    goods_quantity = int(input("Количество товаров: "))
    goods_measure = input("Единица измерения: ")
    goods.append((i, {'название': goods_name, 'цена': goods_price,
                      'количество': goods_quantity, 'eд': goods_measure}))
    i = i + 1
print(f"Исходный список товаров: \n{goods}")

goods_names = []
goods_prices = []
goods_quantities = []
goods_measures = []
for i in goods:
    goods_names.append(i[1].get('название'))
    goods_prices.append(i[1].get('цена'))
    goods_quantities.append(i[1].get('количество'))
    goods_measures.append(i[1].get('eд'))

analytics = {
    'название': list(set(goods_names)),
    'цена': list(set(goods_prices)),
    'количество': list(set(goods_quantities)),
    'eд': list(set(goods_measures))
}
print(f"Аналитика о товарах: \n{analytics}")