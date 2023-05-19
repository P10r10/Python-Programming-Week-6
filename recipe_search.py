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
                result.append(f"{recipes[i - 1]}, preparation time {recipes[i]} min")
        return result

found_recipes = search_by_time("recipes1.txt", 61)

for recipe in found_recipes:
    print(recipe)
