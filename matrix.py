def helper(lst: list, op: str):  # input: list of lists containing integers
    if op == "row_sums":
        return [sum(row) for row in lst]
    elif op == "matrix_sum":
        return sum([sum(row) for row in lst])
    elif op == "matrix_max":
        return max([max(row) for row in lst])


def read_file() -> list:
    result = []
    with open("matrix.txt") as fp:
        for line in fp:
            result.append([int(value) for value in line.split(",")])
    return result


def matrix_sum():
    return helper(read_file(), "matrix_sum")


def row_sums():
    return helper(read_file(), "row_sums")


def matrix_max():
    return helper(read_file(), "matrix_max")


if __name__ == "__main__":
    print(matrix_sum())
    print(row_sums())
    print(matrix_max())
