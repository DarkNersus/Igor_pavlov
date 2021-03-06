'''
2. Дан список:
['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

Необходимо его обработать — обособить каждое целое число кавычками и дополнить нулём до двух разрядов:
['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"', '+05', '"', 'градусов']

Новый список не создавать! Сформировать из обработанного списка строку:
в "05" часов "17" минут температура воздуха была "+05" градусов
'''

list_hw = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

for el in range(len(list_hw)):

    if not list_hw[el].isalpha():

        if '+' in list_hw[el]:
            list_hw[el] = f'"+{int(list_hw[el]):02}"'
        elif '-' in list_hw[el]:
            list_hw[el] = f'"{int(list_hw[el]):02}"'
        else:
            list_hw[el] = f'"{int(list_hw[el]):02}"'

    else:
        continue

print(*list_hw)
