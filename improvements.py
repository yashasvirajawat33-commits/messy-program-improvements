students = [
    ["Rahul", 78, 88, 92],
    ["Priya", 65, 71, 69],
    ["Amit", 90, 94, 85],
    ["Sneha", 55, 60, 58],
    ["Vikram", 82, 79, 88]
]

subjects = ["Python", "Maths", "ML"]


def calculate_total(marks):
    return sum(marks)



def calculate_average(marks):
    return calculate_total(marks) / len(marks)


def calculate_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"



def calculate_result(marks):
    if all(mark >= 40 for mark in marks):
        return "Pass"
    return "Fail"



print("=" * 85)
print("                         STUDENT REPORT CARD")
print("=" * 85)

print(
    f"{'Rank':<6}{'Name':<12}{'Python':<10}"
    f"{'Maths':<10}{'ML':<10}{'Total':<10}"
    f"{'Average':<12}{'Grade':<8}{'Result':<8}"
)
print("-" * 85)


ranked_students = sorted(
    students,
    key=lambda student: calculate_average(student[1:]),
    reverse=True
)

class_total = 0

for rank, student in enumerate(ranked_students, start=1):
    name = student[0]
    marks = student[1:]

    total = calculate_total(marks)
    average = calculate_average(marks)
    grade = calculate_grade(average)
    result = calculate_result(marks)

    class_total += total

    print(
        f"{rank:<6}{name:<12}"
        f"{marks[0]:<10}{marks[1]:<10}{marks[2]:<10}"
        f"{total:<10}{average:<12.2f}{grade:<8}{result:<8}"
    )


class_average = class_total / (len(students) * len(subjects))

print("-" * 85)
print(f"Class Average per Subject: {class_average:.2f}")


topper = ranked_students[0]
lowest = ranked_students[-1]

print(f"Topper: {topper[0]} ({calculate_average(topper[1:]):.2f})")
print(f"Lowest Scorer: {lowest[0]} ({calculate_average(lowest[1:]):.2f})")


print("\nSUBJECT-WISE AVERAGES")

for i, subject in enumerate(subjects):
    subject_total = sum(student[i + 1] for student in students)
    subject_average = subject_total / len(students)
    print(f"{subject}: {subject_average:.2f}")


passed = sum(
    1 for student in students
    if calculate_result(student[1:]) == "Pass"
)

failed = len(students) - passed

print("\nCLASS SUMMARY")
print(f"Total Students: {len(students)}")
print(f"Passed Students: {passed}")
print(f"Failed Students: {failed}")
print("=" * 85)
