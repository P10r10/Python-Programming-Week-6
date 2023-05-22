while True:
    option = input("1 - add an entry, 2 - read entries, 0 - quit\nFunction: ")
    if option == "0":
        print("Bye now!")
        break
    if option == "1":
        entry = input("Diary entry: ")
        with open("diary.txt", "a") as fp:
            fp.write(entry + "\n")
        print("Diary saved")
    if option == "2":
        print("Entries:")
        with open("diary.txt") as fp:
            for row in fp:
                print(row.strip())
