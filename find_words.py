def get_words_from_file() -> list:
    with open("words.txt") as words_file:
        return [line.strip() for line in words_file]


def find_words(search_term: str) -> list:
    result = []
    for word in get_words_from_file():
        split = search_term.split(".")
        if (
            word == search_term
            or (search_term[-1] == "*" and word.startswith(search_term[:-1]))
            or (search_term[0] == "*" and word.endswith(search_term[1:]))
            or (word.startswith(split[0])
                and word.endswith(split[-1])
                # and split[1] == word[len(split[0])+1: len(word)-len(split[2])-1]
                and len(word) == len(search_term))
        ):
            result.append(word)
    return result


print(find_words("c.d."))
