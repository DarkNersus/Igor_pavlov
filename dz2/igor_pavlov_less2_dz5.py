'''
Создать вручную список, содержащий цены на товары (10–20 товаров), например:

[57.8, 46.51, 97, ...]

Вывести на экран эти цены через запятую в одну строку, цена должна отображаться в виде <r> руб <kk> коп
 (например «5 руб 04 коп»). Подумать, как из цены получить рубли и копейки, как добавить нули, если, например,
  получилось 7 копеек или 0 копеек (должно быть 07 коп или 00 коп).
Вывести цены, отсортированные по возрастанию, новый список не создавать (доказать, что объект списка после сортировки
остался тот же).
Создать новый список, содержащий те же цены, но отсортированные по убыванию.
Вывести цены пяти самых дорогих товаров. Сможете ли вывести цены этих товаров по возрастанию, написав минимум кода?
'''

price_list = [109.47, 67.99, 99, 33.9, 47.77, 129.57, 27.89, 49, 93.7, 17.67, 56.09]
price_list.sort()
print(price_list)
for price in price_list:
    cash = int(price)
    cent = int(round(price % 1, 2) * 100)
    if cent < 10:
        cent = str(f"0{cent}")
    print(f"{cash} рублей {cent} копеек.")

print('-' * 140)

print('Сортировка от меньшего к большему:', price_list, 'id:', id(price_list))
print('Сортировка от большего к меньшему:', sorted(price_list, reverse=True), 'id:', id(price_list))

print('-' * 140)

new_price = sorted(price_list, reverse=True)
print(new_price)

print('-' * 140)

for i, top in enumerate(price_list[:5]):
    print(f"Топ {i + 1} по саммой низкой ценне. {top} ")

print('-' * 40)

for i, top in enumerate(new_price[:5]):
    print(f"Топ {i + 1} по саммой высокой ценне. {top} ")