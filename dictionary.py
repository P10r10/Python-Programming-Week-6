def add_word():
    word_fi = input("The word in Finnish: ")
    word_en = input("The word in English: ")
    if word_fi in read_file():
        return
    with open("dictionary.txt", "a") as file:
        file.write(f"{word_fi};{word_en}\n")
    print("Dictionary entry added")


def search_term():
    search = input("Search term: ")
    for word, meaning in read_file().items():
        if search in word or search in meaning:
            print(f"{word} - {meaning}")


def menu():
    while True:
        print("1 - Add word, 2 - Search, 3 - Quit")
        option = input("Function: ")
        if option == "3":
            print("Bye!")
            break
        if option == "1":
            add_word()
        if option == "2":
            search_term()


def read_file() -> dict:
    with open("dictionary.txt") as file:
        return {l.split(";")[0]: l.split(";")[1].strip() for l in file}


menu()
