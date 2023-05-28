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
course_file = input("Course information: ")
with open("course1.txt") as course_file:
    course = course_file.readline().split(":")[1].strip()
    print(course)
    credits = int(course_file.readline().split(":")[1])
with open("results.txt", "w") as res_txt, open("results.csv", "w") as res_csv:
    header = f"{course}, {credits} credits"
    res_txt.write(f"{header}\n{'=' * len(header)}\n")
    headers = ["name", "exec_nbr", "exec_pts.",
               "exm_pts.", "tot_pts.", "grade"]
    res_txt.write(f"{headers[0]:30}")
    res_txt.write("".join(f"{header:10}" for header in headers[1:]))
    for id, name in read_file(student_file, "students").items():
        exerc = sum(read_file(exercises_file)[id])
        exams = sum(read_file(exam_file)[id])
        res_txt.write(f"\n{name:30}{exerc:<10}{exerc//4:<10}{exams:<10}"
                      f"{exerc//4 + exams:<10}"
                      f"{get_final_grade(exerc//4 + exams):<10}")
        res_csv.write(f"{id};{name};{get_final_grade(exerc//4 + exams)}\n")
print("Results written to files results.txt and results.csv")
