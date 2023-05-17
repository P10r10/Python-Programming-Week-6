# Please write a program which asks the user to type in some text. Your program
# should then perform a spell check, and print out feedback to the user, so
# that all misspelled words have stars around them.

text = input("Write text: ")
with open("wordlist.txt") as fp:
    dictionary = [word.strip().upper() for word in fp]
for word in text.split(" "):
    print(f"{word} ", end="") if word.upper() in dictionary else print(f"*{word}* ", end="")
