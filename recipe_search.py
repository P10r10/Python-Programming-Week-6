def get_recipes(filename: str) -> list:
    with open(filename) as fp:
        recipes = [row.strip() for row in fp]
        names = []
        names.append(recipes[0])
        for i in range(1, len(recipes)):
            if recipes[i] == "":
                names.append(recipes[i + 1])
        return names


def search_by_name(filename: str, word: str) -> list:
    names = get_recipes(filename)
    result = []
    for name in names:
        if word.upper() in name.upper():
            result.append(name)
    return result


def search_by_time(filename: str, prep_time: int):
    with open(filename) as fp:
        recipes = [row.strip() for row in fp]
        result = []
        for i in range(len(recipes)):
            if recipes[i].isdigit() and int(recipes[i]) <= prep_time:
                result.append(
                    f"{recipes[i - 1]}, preparation time {recipes[i]} min")
        return result


def search_by_ingredient(filename: str, ingredient: str):
    with open(filename) as fp:
        lines = [row.strip() for row in fp]
        lines.append("")
    recipes = []
    recipe = []
    for row in lines:
        if row != "":
            recipe.append(row)
        else:
            recipes.append(recipe.copy())
            recipe.clear()
    result = []
    for recipe in recipes:
        if ingredient in recipe:
            result.append(f"{recipe[0]}, preparation time {recipe[1]} min")
    return result


if __name__ == "__main__":
    found_recipes = search_by_ingredient("recipes1.txt", "eggs")

    for recipe in found_recipes:
        print(recipe)
