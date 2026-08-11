"""
Print Multiplication Table of 1000 up to 10
-------------------------------------------
This script prints the mathematical table of 1000 from 1 to 10 using a for loop.
"""

number = 1000


for i in range(1, 11):
    result = number * i
    print(f"{number} x {i} = {result}")

studnt = {"name": "abhay", "roll": 101, "age": 26}
for key, value in studnt.items():
    print(f"Key: {key} -> Value: {value}")

