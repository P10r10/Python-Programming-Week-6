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


# student_file = input("Student information: ")
# exercises_file = input("Exercises completed: ")
# exam_file = input("Exam points: ")
student_file = "students1.csv"
exercises_file = "exercises1.csv"
exam_file = "exam_points1.csv"
course = "Introduction to Programming"
credits = 5
header = f"{course}, {credits} credits"
print(f"{header}\n{'=' * len(header)}")
headers = ["name", "exec_nbr", "exec_pts.", "exm_pts.", "tot_pts.", "grade"]
print(f"{headers[0]:30}", end="")
print("".join(f"{header:10}" for header in headers[1:]))
for id, name in read_file(student_file, "students").items():
    exerc = sum(read_file(exercises_file)[id])
    exams = sum(read_file(exam_file)[id])
    print(f"{name:30}{exerc:<10}{exerc // 4:<10}{exams:<10}"
          f"{exerc // 4 + exams:<10}{get_final_grade(exerc // 4 + exams):<10}")
