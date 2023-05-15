def read_file(file_name: str, what=None) -> dict:
    res = {}
    with open(file_name) as fp:
        for line in fp:
            split = line.split(";")
            if split[0] == "id":
                continue
            if what == None:
                res[int(split[0])] = [int(nb) for nb in split[1:]]
            elif what == "students":
                res[int(split[0])] = split[1] + " " + split[2].strip()
    return res

def get_final_grade(points: int) -> int:
    values = [14, 17, 20, 23, 27]
    for i in range(5):
        if points <= values[i]:
            return i
    return 5

student_file = input("Student information: ")
exercises_file = input("Exercises completed: ")
exam_file = input("Exam points: ")
for id, name in read_file(student_file, "students").items():
    total = 0
    if id in read_file(exercises_file):
        total += sum(read_file(exercises_file)[id]) // 4
    if id in read_file(exam_file):
        total += sum(read_file(exam_file)[id])
    print(f"{name} {get_final_grade(total)}")
