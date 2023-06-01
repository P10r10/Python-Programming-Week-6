names = ["alex", "bruno", "admin", "pedro", "joão", "miguel"]
if names:
    for name in names:
        if name == "admin":
            print("Hello admin, would you like to see a report?")
        else:
            print(f"Hello {name}, you're logged in now.")
else:
    print("We need to find some users!")
current_users = ["Alex", "bruno", "admin", "pedro", "joão", "Miguel"]
new_users = ["filipe", "santiago", "Admin", "humberto", "maria", "miguel"]
current_users_lower = [user.lower() for user in current_users]
for user in new_users:
    if user.lower() in current_users_lower:
        print(f"the name {user} is taken.")
    else:
        print(f"the name {user} is available.")
numbers = [n for n in range(1, 10)]
for number in numbers:
    if number == 1:
        print(f"{number}st")
    elif number == 2:
        print(f"{number}nd")
    elif number == 3:
        print(f"{number}rd")
    else:
        print(f"{number}th")
# print("DEB", numbers)