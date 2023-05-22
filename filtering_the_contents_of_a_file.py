def filter_solutions():
    with open("solutions.csv") as sol_file, open("correct.csv", "w") as corr_file, open("incorrect.csv", "w") as inc_file:
        correct = False  # holds the result of test for correct answers
        for row in sol_file:
            split = row.split(";")
            operation = split[1]  # holds both operands and one operator
            if "-" in operation:
                a, b = operation.split("-")  # a and b are the operands
                correct = int(a) - int(b) == int(split[2])  # holds the result
            elif "+" in operation:
                a, b = operation.split("+")  # a and b are the operands
                correct = int(a) + int(b) == int(split[2])  # holds the result
            if correct:
                corr_file.write(row)
            else:
                inc_file.write(row)


filter_solutions()
