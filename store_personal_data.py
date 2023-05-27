def store_personal_data(person: tuple):
    with open("people.csv", "a") as fp:
        fp.write(f"{person[0]};{person[1]};{person[2]}\n")


store_personal_data(("Janet Jackson", 51, 155))
