def get_words_from_file() -> list:
    with open("words.txt") as words_file:
        return [line.strip() for line in words_file]


def find_words(search_term: str) -> list:
    result = []
    for word in get_words_from_file():
        if (
            word == search_term
            or (search_term[-1] == "*" and word.startswith(search_term[:-1]))
            or (search_term[0] == "*" and word.endswith(search_term[1:]))
            or (word.startswith(search_term.split(".")[0])
                and word.endswith(search_term.split(".")[-1])
                and len(word) == len(search_term))
        ):
            result.append(word)
    return result

print(find_words("c.d."))
# Search term c.d. should return 7 lines