my_dict = {'Danil': 1995, 'Viktoria': 1998, 'Aleksei': 1988, 'Vladislav':1989 }
print(my_dict)
print(my_dict.get('Danil', 'Такого ключа нет'))
print(my_dict.get('Nikita',  'Такого ключа нет'))
my_dict.update({'Sergey': 1992, 'Max': 1996})
print(my_dict)
a = my_dict.pop('Aleksei')
print(my_dict)
print(a)

my_set = {1, 5, 6, 2, 1, 5, 6, 3, 4, 8, 4, 5, 4, 6, 'String', False, True}
print(my_set)  
my_set.add(7)
print(my_set)
my_set.discard(4)
print(my_set)
