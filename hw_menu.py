from pprint import pprint

import os
path = os.path.join(os.getcwd(), 'data_hw1.txt')

with open(path, encoding='utf-8') as file:
      result = {}
      for dish in file:
         dish_name = dish.strip()
         counter = int(file.readline().strip())
         temp_data = []
         for item in range(counter):
              ingredient_name, quantity, measure = file.readline().strip().split('|')
              temp_data.append({'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure})
              result[dish_name] = temp_data
              file.readline()
              print(result)





cook_book = {
   'Омлет': [
     {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},
     {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
     {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
     ],
   'Утка по-пекински': [
     {'ingredient_name': 'Утка', 'quantity': 1, 'measure': 'шт'},
     {'ingredient_name': 'Вода', 'quantity': 2, 'measure': 'л'},
     {'ingredient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'},
     {'ingredient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}
     ],
   'Запеченный картофель': [
     {'ingredient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
     {'ingredient_name': 'Чеснок', 'quantity': 3, 'measure': 'зубч'},
     {'ingredient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'},
     ]
   }


def get_shop_list_by_dishes(dishes, person_count):
     new_list = {}
     for dish in dishes:
         # if i in cook_book:
         for i in cook_book[dish]:
             if i['ingredient_name'] in new_list.keys():
                 new_list[i['ingredient_name']]['quantity'] += i['quantity']
             else:
                 new_list[i['ingredient_name']] = {}
                 new_list[i['ingredient_name']]['measure'] = i['measure']
                 new_list[i['ingredient_name']]['quantity'] = i['quantity'] * person_count

                 print(new_list)


print (get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))

