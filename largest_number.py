def largest() -> int:
    with open("numbers.txt") as fp:
        largest = int(fp.readline())
        for line in fp:
            if int(line) > largest:
                largest = int(line)
    return largest


if __name__ == "__main__":
    print(largest())
