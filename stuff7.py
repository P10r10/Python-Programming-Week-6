person1 = {
    "first_name": "Alex",
    "last_name": "Almeida",
    "city": "Porto",
    "age": 49,
}

for k, v in person1.items():
    print(k, v)

countries = {
    "portugal": "lisbon",
    "spain": "madrid",
    "france": "paris",
    "germany": "berlin",
    "belgium": "bruxels",
    "mali": "bamaco",
    "italy": "rome",
    "croatia": "zagreb",
    "morocco": "rabat",
    "chile": "santiago",

}

for country, capital in countries.items():
    print(f"The capital of {country.title()} is {capital.title()}.")
for country in countries.keys():
    print(country.title())
for capital in countries.values():
    print(capital.title())

people = ["alice", "peter", "john", "elsa"]
persons = {
    "alice": "lisbon",
    "bob": "madrid",
    "michael": "paris",
    "jeremy": "berlin",
    "elsa": "bruxels",
}
for name in people:
    if name in persons:
        print(f"Thank you for answering the poll, {name.title()}!")
    else:
        print(f"Hi, {name.title()}, please answer the poll.")

