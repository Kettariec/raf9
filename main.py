import json


class Raf9:
    def __init__(self):
        self.ingredients = ['ice', 'mint', 'soda',
                            'lemon', 'tomato', 'orange',
                            'sprite', 'sugar']
        self.ingredients.sort()
        with open('cocktails.json', 'r') as json_file:
            self.cocktails = json.load(json_file)

    def __call__(self):
        while True:
            self.__help_text()
            command = input('Введите команду')
            if command == '0':
                print('Всего доброго, приходите ещё!')
                break
            elif command == '1':
                your_ings = self.__choose_ingredients()
                your_ings.sort()
                result = self.find_cocktail(your_ings)
                if len(your_ings) == 0:
                    print('Всего доброго, приходите ещё!')
                    break
                elif result is None:
                    self.save_cocktail(your_ings)
                    print(f'Создан новый коктейль с ингредиентами {your_ings}')
                    break
                else:
                    print(f'Вы выбрали коктейль {result}')
                    break

            else:
                print('Неверная команда')

    def __help_text(self):
        print('Доступные команды:')
        print('1 - выбрать ингредиенты')
        print('0 - выйти')

    def save_cocktail(self, ings):
        self.cocktails.append({
            'name': 'new_cocktail',
            'ingredients': ings
        })

        with open('cocktails.json', 'w') as json_file:
            json.dump(self.cocktails, json_file, ensure_ascii=False, indent=2)

    def find_cocktail(self, ings):
        for c in self.cocktails:
            if c.get('ingredients') == ings:
                return c.get('name')
        return None

    def __choose_ingredients(self):
        chose_ings = []

        i = 0
        for ing in self.ingredients:
            i += 1
            print(f'{i}. {ing}')
        print('0 - для выхода')

        while True:
            command = input('Выберите ингредиент:')
            if command == '0':
                return chose_ings
            else:
                if command.isdigit():
                    number = int(command)
                    if number > len(self.ingredients):
                        print('Такого ингредиента в списке нет')
                    else:
                        chose_ings.append(self.ingredients[number-1])
                else:
                    print('Введите НОМЕР ингредиента')


if __name__ == "__main__":
    raf9 = Raf9()
    raf9()

    assert 'mojito' == raf9.find_cocktail(['ice', 'mint', 'soda'])
