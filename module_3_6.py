def calc_sum_struct(data_structure):
    str_struct = str(data_structure)            #преобразуем введенную структуру в строку
    symbols = "()[]{}:,"
    for i in range(len(symbols)):               #заменяем символы ()[]{}:, на пробелы
        if symbols[i] in str_struct:
            str_struct = str_struct.replace(symbols[i], ' ')
    list_struct = str_struct.split()            #преобразуем в список, удаляя лишние пробелы
    summa = 0
    for i in list_struct:                       #считаем сумму
        if "'" in i:
            summa += len(i.replace("'",""))     #если элемент строковый
        elif "." in i:
            summa += float(i)
        else:
            summa += int(i)
    return summa


result1 = calc_sum_struct([[1, 2, 3],{'a': 4, 'b': 5},(6, {'cube': 7, 'drum': 8}),"Hello",((), [{(2, 'Urban', ('Urban2', 35))}])])
result2 = calc_sum_struct([1, 2.0, 'Anna', {'a': 4, 'b': 5}])
result3 = calc_sum_struct([5,2,"Anna5", [{'ab':4.0, 'cd':5}, 'Vika']])    #проверка "корявого" ввода структуры данных
print(result1)
print(result2)
print(result3)
