import fileinput


class Meal(object):
    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients


def get_unique_meal_count(meals):
    unique_meals = dict()

    for meal in meals:
        if (''.join(meal.ingredients),) not in unique_meals:
            unique_meals[(''.join(meal.ingredients),)] = meal.name

    return len(unique_meals)


if __name__ == "__main__":
    lines = [line.strip() for line in list(fileinput.input())]
    meals = []
    for line in lines:
        meal, ingredients = line.split(' - ')
        ingredients = ingredients.split(',')
        meals.append(Meal(meal, ingredients))
    print(get_unique_meal_count(meals))
