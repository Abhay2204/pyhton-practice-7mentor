odd_numbers = set(range(1, 50, 2))
print("Odd numbers:", odd_numbers)

even_numbers = range(2, 51, 2)
odd_numbers.update(even_numbers)

print("After adding even numbers:", odd_numbers)
