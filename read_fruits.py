# Please write a function named read_fruits, which reads the file and returns
# a dictionary based on the contents. In the dictionary, the name of the fruit
# should be the key, and the value should be its price. Prices should be of type float.

def read_fruits() -> dict:
    result = {}
    with open("fruits.csv") as fp:
        for line in fp:
            split = line.split(";")
            result[split[0]] = float(split[1])
    return result
