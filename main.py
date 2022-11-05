import os
from pprint import pprint

def dict_food():
    file_path = os.path.join(os.getcwd(), file)
    cook_book = {}
    with open(file_path, 'r',encoding ='utf 8' ) as file_copy:
        for line in file_copy:
            food_name = line.strip()
            counter = file_copy.readline().strip()
            ingredients_list = []
            food_name_list =[]
            for item in range(int(counter)):
                food_name_list.append(food_name)
                food_items = dict.fromkeys(['ingredient_name', 'quantity', 'measure'])
                ingredient= file_copy.readline().strip().split(' | ')
                for _ in ingredient:
                    food_items['ingredient_name'] = ingredient[0]
                    food_items['quantity'] = ingredient[1]
                    food_items['measure'] = ingredient[2]
                ingredients_list.append(food_items)
                recept = {food_name: ingredients_list}
                cook_book.update(recept)
            file_copy.readline()
        return cook_book

file ='food_list.txt'
cook_book = dict_food()
print("\nCook_book: \n")
pprint(cook_book, indent=2, width=100, sort_dicts=False)
print()
print("_"*100)

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish_name in dishes:
        if dish_name in cook_book:
            for ingredient in cook_book[dish_name]:
                ingredients_quantity_list = {}
                if ingredient['ingredient_name'] not in shop_list:
                    ingredients_quantity_list['quantity'] = int(ingredient['quantity']) * int(person_count)
                    ingredients_quantity_list['measure'] = ingredient['measure']
                    shop_list[ingredient['ingredient_name']] = ingredients_quantity_list
                else:
                    shop_list[ingredient['ingredient_name']]['quantity'] = shop_list[ingredient['ingredient_name']]['quantity'] + \
                                                                     int(ingredient['quantity']) * int(person_count)
        else:
            print(f'\n"Такого рецепта нет"\n')
    return shop_list

p = person_count = 3
d = dishes = {'Омлет', 'Фахитос', 'Запеченный картофель'}
print('\nДля приготовления выбранных блюд на указанное количество человек необходимо: \n')
pprint(get_shop_list_by_dishes(d,p), indent=6)

print()
print("_"*100)

def sort_file():
    file_name_1 = '1.txt'
    file_name_2 = '2.txt'
    file_name_3 = '3.txt'
    os.chdir('sorted')
    sorted_dict = {}
    new_file = "sorted_file.txt"
    file1_path = os.path.join(os.getcwd(), file_name_1)
    file2_path = os.path.join(os.getcwd(), file_name_2)
    file3_path = os.path.join(os.getcwd(), file_name_3)
    with open(file1_path, 'r', encoding='utf-8') as f1:
        file1 = f1.readlines()
    with open(file2_path, 'r', encoding='utf-8') as f2:
        file2 = f2.readlines()
    with open(file3_path, 'r', encoding='utf-8') as f3:
        file3 = f3.readlines()
    sorted_dict[file_name_1] = len(file1)
    sorted_dict[file_name_2] = len(file2)
    sorted_dict[file_name_3] = len(file3)
    sorted_tuple=sorted(sorted_dict.items(), key=lambda x:x[1])
    sorted_list = list(sorted_tuple)
    file_first_path = os.path.join(os.getcwd(), sorted_list[0][0])
    file_two_path = os.path.join(os.getcwd(), sorted_list[1][0])
    file_three_path = os.path.join(os.getcwd(), sorted_list[2][0])
    with open(file_first_path, 'r', encoding='utf-8') as f_first:
        file_first = f_first.readlines()
    with open(file_two_path, 'r', encoding='utf-8') as f_two:
        file_two = f_two.readlines()
    with open(file_three_path, 'r', encoding='utf-8') as f_three:
        file_three = f_three.readlines()
    with open(new_file, 'w', encoding='utf-8') as f_all:
        f_all.write(str(sorted_list[0][0]) +'\n')
        f_all.write('Количество строк: ' + str(sorted_list[0][1]) + '\n\n')
        f_all.writelines(file_first)
        f_all.write('\n\n')
        f_all.write(sorted_list[1][0] + '\n')
        f_all.write('Количество строк: ' + str(sorted_list[1][1]) + '\n\n')
        f_all.writelines(file_two)
        f_all.write('\n\n')
        f_all.write(sorted_list[2][0] + '\n')
        f_all.write('Количество строк: ' + str(sorted_list[2][1]) + '\n\n')
        f_all.writelines(file_three)
        f_all.write('\n\n')
    return
sort_file()


