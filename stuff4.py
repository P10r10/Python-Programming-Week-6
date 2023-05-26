for n in range(1, 21):
    print(n, " ", end="")
million = [n for n in range(1, 1_000_001)]
print("\nmin: ", min(million))
print("max: ", max(million))
print("sum: ", sum(million))
odd = [n for n in range(1, 21, 2)]
mult_of_3 = [n for n in range(3, 31, 3)]
cubes = [n**3 for n in range(1, 11)]
ten = [n for n in range(1, 11)]
print(f"The 1st three items in the list are {ten[:3]}.")
print(f"The three items in the middle of the list are {ten[3:6]}.")
print(f"The last three items in the list are {ten[-3:]}.")
pizzas = ["pepperoni", "napolitana", "cheeseham"]
friends_pizzas = pizzas.copy()
pizzas.append("Bacana")
friends_pizzas.append("Special")
print(pizzas)
print(friends_pizzas)
buffet = "bitoque", "picanha", "leitão", "caril", "francesinha"
for dish in buffet:
    print(dish)
buffet = "crepes", "picanha", "leitão", "frango", "francesinha"
print(buffet)