def get_recipes(file: str) -> list:
    with open(file) as fp:
        return [row.strip() for row in fp]

def search_by_name(filename: str, word: str) -> list:
    with open(filename) as fp:
        recipes = [row.strip() for row in fp]
        names = []
        names.append(recipes[0])
        for i in range(1, len(recipes)):
            if recipes[i] == "":
                names.append(recipes[i + 1])
    result = []
    for name in names:
        if word.upper() in name.upper():
            result.append(name)
    return result

print(search_by_name("recipes1.txt", "cake"))