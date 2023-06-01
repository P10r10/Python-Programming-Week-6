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
        ):
            result.append(word)
    return result


# print(find_words("*ulet"))
words = [".."]

for c in range(97, 123):
    words.append(words[0].replace(".", chr(c), 1))
# del(words[0])
words.remove("..")
for word in words:
    if "." in word:
        for c in range(97, 123):
            words.append(word.replace(".", chr(c), 1))
        words.remove(word)
print(words)       

# for letter in word:
#     if letter == ".":
# TODO arranjar algoritmo para substituição do "."
