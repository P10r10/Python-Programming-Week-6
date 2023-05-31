alien_color = "red"
points = 0
if alien_color == "green":
    points = 5
elif alien_color == "yellow":
    points = 10
elif alien_color == "red":
    points = 15
print(f"You won {points} points!")
age = 80
if age < 2:
    print("You're a baby!")
elif age < 4:
    print("You're a toddler.")
elif age < 13:
    print("You're a kid.")
elif age < 20:
    print("You're a teenager.")
elif age < 65:
    print("You're an adult.")
else:
    print("You're an elser.")
fruits = ["mango", "banana", "peach"]
if "banana" in fruits:
    print("You really like bananas!")
