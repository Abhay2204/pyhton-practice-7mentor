"""
Python Dictionaries Practice Questions
---------------------------------------
This file contains practice questions covering creation, accessing, safe lookups,
modifications, dictionary methods, and dictionary iterations.
"""

# ==========================================
# 1. DICTIONARY CREATION & ACCESSING
# ==========================================

student = {
    "name": "Alex",
    "age": 20,
    "grade": "A",
    "courses": ["Math", "Physics"]
}

print("Name:", student["name"])
print("Age (via .get()):", student.get("age"))
print("2nd Course:", student["courses"][1])


# ==========================================
# 2. DICTIONARY MODIFICATION & METHODS
# ==========================================

student["city"] = "New York"
print("After adding city:", student)

student["age"] = 21
print("After updating age:", student)

removed_grade = student.pop("grade")
print("Removed grade:", removed_grade)

print("Keys:", list(student.keys()))
print("Values:", list(student.values()))

print("\nKey-Value Pairs:")
for key, val in student.items():
    print(f"  {key}: {val}")


# ==========================================
# 3. SIMPLE DICT & MARKS
# ==========================================

a = {"name": "abhay", "marks": 99}
print("\nSimple dict 'a':", a)
