def read_input(prompt: str, a: int, b: int):
    while True:
        try:
            n = int(input(prompt))
            if n >= a and n <= b:
                return n
        except:
            pass
        print(f"You must type in an integer between {a} and {b}")


number = read_input('Enter a number', 1, 5)
print("You typed in:", number)
