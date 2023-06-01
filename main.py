students = {}
n = int(input("Введіть кількість студентів: "))
for _ in range(n):
    name = input("Введіть ім'я студента: ")
    grade = float(input("Введіть оцінку з математики: "))
    students[name] = grade
max_grade = max(students.values())
top_student = [name for name, grade in students.items() if grade == max_grade]
print("Студент(и) з найвищою оцінкою:")
for student in top_student:
    print(student)
