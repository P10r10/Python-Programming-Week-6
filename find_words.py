def find_words(search_term: str) -> list:
    result = []
    with open("words.txt") as words_file:
        words = [line.strip() for line in words_file]
    for word in words:
        if word == search_term:
            result.append(word)
        if search_term[-1] == "*" and word.startswith(search_term[:-1]):
            result.append(word)
        if search_term[0] == "*" and word.endswith(search_term[1:]):
            result.append(word)
    return result
