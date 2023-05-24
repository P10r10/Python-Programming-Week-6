guests = ["Leonardo da Vinci", "Isaac Newton", "Nikola Tesla"]
for guest in guests:
    print(
        f"Dear {guest}, I admire you deeply and would like to invite you to dinner.")
name = "Isaac Newton"
print(f"{name} can't make it. How unfortunate.\n")
new_guest = "Garry Kasparov"
guests.remove(name)
guests.append(new_guest)
for guest in guests:
    print(guest)
print("I found a bigger table!")
guests.insert(0, "Johann Goethe")
guests.insert(len(guests) // 2, "Nicolaus Copernicus")
guests.append("William Shakespeare")
for guest in guests:
    print(guest)
print(f"I'm inviting {len(guests)} guests.")
print("Alas, there is only room for two. :(")
while len(guests) > 2:
    print(f"Dear {guests.pop()}, I'm sorry but I can't invite you to dinner.")
for guest in guests:
    print(f"Dear {guest}, you're still invited.")
del guests[0]
del guests[0]
print(guests)