from operations import add, multiply

def add_even(numbers):
    total = 0
    for n in numbers:
        if n % 2 == 0:
            total = add(total, n)
    return total

def mul_odd(numbers):
    result = 1
    for n in numbers:
        if n % 2 != 0:
            result = multiply(result, n)
    return result

numbers = [1, 2, 3, 4, 5, 6, 7]

print("Numbers:", numbers)
print("Sum of even numbers:", add_even(numbers))
print("Multiplication of odd numbers:", mul_odd(numbers))

