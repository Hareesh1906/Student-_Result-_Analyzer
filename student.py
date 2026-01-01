# Student Result Analyzer with SGPA Calculation 

name = input("Enter student name: ")

marks = []
grade_points = []

for i in range(5):
    m = int(input("Enter mark: "))
    marks.append(m)

    if m >= 90:
        grade = "O"
        gp = 10
    elif m >= 80:
        grade = "A+"
        gp = 9
    elif m >= 70:
        grade = "A"
        gp = 8
    elif m >= 60:
        grade = "B+"
        gp = 7
    elif m >= 50:
        grade = "B"
        gp = 5
    elif m >= 45:
        grade = "C"
        gp = 4
    elif m >= 40:
        grade = "P"
        gp = 0
    else:
        grade = "F"
        gp = 0

    grade_points.append(gp)
    print("Subject", i+1, "Grade:", grade)

sgpa = sum(grade_points) / len(grade_points)

print("\nName:", name)
print("Marks:", marks)
print("Grade Points:", grade_points)
print("SGPA:", round(sgpa, 2))
