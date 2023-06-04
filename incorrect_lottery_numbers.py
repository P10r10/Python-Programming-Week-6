def filter_incorrect():
    with open("lottery_numbers.csv") as lottery_file,\
            open("correct_numbers.csv", "w") as correct_file:
        for line in lottery_file:
            try:
                week = int(line.split(";")[0].split(" ")[1])
                numbers = line.split(";")[1].split(",")
                numbers_int = [int(n) for n in numbers]  # tests for ints
                if len(numbers_int) != 7:
                    raise Exception
                for n in numbers_int:
                    if n < 1 or n > 39:
                        raise Exception
                if len(set(numbers_int)) != 7:
                    raise Exception
                correct_file.write(f"week {week};{line.split(';')[1]}")

            except:
                pass


filter_incorrect()
