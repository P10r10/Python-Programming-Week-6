def read_students(file_name: str) -> dict:
    students = {}
    with open(file_name) as fp:
        for line in fp:
            split = line.split(";")
            if split[0] == "id":
                continue
            students[int(split[0])] = split[1] + " " + split[2].strip()
    return students


def read_exercises(file_name: str) -> dict:
    exercises = {}
    with open(file_name) as fp:
        for line in fp:
            split = line.split(";")
            if split[0] == "id":
                continue
            exercises[int(split[0])] = [int(nb) for nb in split[1:]]
    return exercises


student_file = input("Student information: ")
exercises_file = input("Exercises completed: ")
for id, name in read_students(student_file).items():
    if id in read_exercises(exercises_file):
        print(name, sum(read_exercises(exercises_file)[id]))