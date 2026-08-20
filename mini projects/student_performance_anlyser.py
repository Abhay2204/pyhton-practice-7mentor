students = []

# Take student information
number = int(input("How many students? "))

for i in range(number):
    name = input("Enter student name: ")
    score = int(input("Enter student score: "))

    student = {
        "name": name,
        "score": score
    }

    students.append(student)


# Lists for passed and failed students
passed = []
failed = []


# Calculate grades
for student in students:
    name = student["name"]
    score = student["score"]

    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 50:
        grade = "D"
    else:
        grade = "F"

    print(name, "-", score, "-", grade)

    # Separate students
    if score >= 50:
        passed.append(name)
    else:
        failed.append(name)


# Display results
print("\nPassed Students:", passed)
print("Students Needing Help:", failed)