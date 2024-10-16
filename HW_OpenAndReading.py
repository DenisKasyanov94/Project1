def is_closed(file):
  if file.closed:
    print('Файл закрыт')
  else:
    print('Файл открыт')


def read_recipes(file_path):
  cook_book = {}
  with open(file_path, encoding='UTF-8') as file:
    is_closed(file)
    content = file.read().strip().split('\n\n')

    for recipe in content:
      lines = recipe.strip().split('\n')
      title = lines[0]
      ingredient_count = int(lines[1])
      ingredients = []

      for i in range(2, 2 + ingredient_count):
        name, amount, unit = lines[i].split(' | ')
        ingredients.append({
          'ingredient_name': name,
          'quantity': int(amount),
          'measure': unit
        })

      cook_book[title] = ingredients

    is_closed(file)
  return cook_book


def display_cook_book(cook_book):
  for recipe, ingredients in cook_book.items():
    print(f"Рецепт: {recipe}")
    for ingredient in ingredients:
      print(f"- {ingredient['ingredient_name']}: {ingredient['quantity']} {ingredient['measure']}")
    print()


def get_shop_list_by_dishes(dishes, person_count, cook_book):
  shop_list = {}

  for dish in dishes:
    if dish in cook_book:
      for ingredient in cook_book[dish]:
        name = ingredient['ingredient_name']
        quantity = ingredient['quantity'] * person_count
        measure = ingredient['measure']


        if name in shop_list:
          shop_list[name]['quantity'] += quantity
        else:
          shop_list[name] = {'measure': measure, 'quantity': quantity}
    else:
      print(f"Блюдо {dish} не найдено в книге рецептов")

  return shop_list


def display_shop_list(shop_list):
  print("Список покупок:")
  for ingredient, details in shop_list.items():
    print(f"{ingredient}: {details['quantity']} {details['measure']}")
  print()


def main():
  file_path = 'cook_book.txt'
  cook_book = read_recipes(file_path)
  display_cook_book(cook_book)


  dishes = ['Омлет', 'Утка по-пекински']
  person_count = 3

  shop_list = get_shop_list_by_dishes(dishes, person_count, cook_book)
  display_shop_list(shop_list)


if __name__ == "__main__":
  main()



