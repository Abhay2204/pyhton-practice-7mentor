"""
09. Dictionaries - Code Examples
--------------------------------
Demonstrates safe dictionary lookup, frequency counters, and nested dictionary access.
"""

# 1. Safe Lookup & Modification
student = {
    "name": "Abhay",
    "marks": 99,
    "courses": ["Math", "Python", "SQL"]
}

print("=== Safe Access ===")
print("Name:", student.get("name"))
print("2nd Course:", student["courses"][1])
print("Scholarship:", student.get("scholarship", "Not Eligible"))

# 2. Word Frequency Counter
text = "apple banana apple cherry banana apple"
words = text.split()
freq_map = {}
for word in words:
    freq_map[word] = freq_map.get(word, 0) + 1

print("\n=== Word Frequency Counter ===")
print(freq_map)

# 3. Nested Dictionary Iteration
company = {
    "emp1": {"name": "Alice", "role": "Dev"},
    "emp2": {"name": "Bob", "role": "QA"}
}

print("\n=== Nested Dictionary Iteration ===")
for emp_id, info in company.items():
    print(f"{emp_id}: {info['name']} ({info['role']})")
