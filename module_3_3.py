def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)


print_params()
print_params('Колобок', 1, 2)
print_params(b=25)
print_params(c = [1,2,3])
values_list=[True, 'Колобок', 25]
values_dict={'a': False, 'b': 'Лиса', 'c': 52}
print_params(*values_list)
print_params(**values_dict)
values_list_2=['Волк', 81]
print_params(*values_list_2, 42)