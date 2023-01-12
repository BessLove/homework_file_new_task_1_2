from pprint import pprint
file_path = 'text.txt'
def make_cook_book(name_file):
    recipes = {}
    with open(name_file, encoding='UTF-8') as file:
        for string in file:
            dish = string.strip()
            ingred_quant = int(file.readline())
            ingreds = []
            for i in range(ingred_quant):
                ingr = file.readline().split(' | ')
                ingredients = {'ingredient_name': ingr[0].strip(), 'quantity': int(ingr[1]), 'measure': ingr[2].strip()}
                ingreds.append(ingredients)
            recipes[dish] = ingreds
            file.readline()
    return recipes

# pprint(make_cook_book(file_path), width=70)

def get_shop_list_by_dishes(dishes: list, person_count=1, file_path = 'text.txt'):
    cook_book = make_cook_book(file_path)
    shop_list = {}
    for dish in dishes:
        if dish not in cook_book:
            return (f"Блюда {dish} нет в списке рецептов. Проверьте запись и попробуйте заново")
        for ingredient in cook_book[dish]:
            name = ingredient.get('ingredient_name', [])
            quantity = ingredient.get('quantity', [])
            measure = ingredient.get('measure', [])
            if name in shop_list:
                shop_list[name]['quantity'] += quantity * person_count
            else:
                shop_list[name] = {'quantity': quantity * person_count, 'measure': measure}

    return shop_list
print(get_shop_list_by_dishes(['Фахитос', 'Омлет'], 2))

