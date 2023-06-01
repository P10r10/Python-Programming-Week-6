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
    "espanha": "madrid",
    "frança": "paris",
    "alemanha": "berlin",
    "bélgica": "bruxels",
}

for country, capital in countries.items():
    print(f"The capital of {country.title()} is {capital.title()}.")
