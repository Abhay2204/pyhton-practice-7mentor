"""
Python String Practice Questions
--------------------------------
This file contains various basic-to-intermediate string practice questions 
covering all major string concepts in Python.

Try solving each question below by writing your code where indicated.
"""

# ==========================================
# 1. STRING CREATION & INDEXING
# ==========================================

# Q1: Given the string below, print the first and the last character.
text = "Python Programming"
# Your code here:
print("First character:", text[0])
print("Last character:", text[-1])

# Q2: Print the character at index 7 of the string 'text'.
# Your code here:
print(text[7])

# Q3: Print the 3rd character from the end using negative indexing.
# Your code here:
print(text[-3])

# ==========================================
# 2. STRING SLICING
# ==========================================

word = "Antigravity"

# Q4: Slice and print the first 4 characters of 'word' ("Anti").
# Your code here:
print(word[:4])

# Q5: Slice and print characters from index 4 to the end ("gravity").
# Your code here:
print(word[4:])

# Q6: Reverse the string 'word' using slicing.
# Your code here:
print(word[::-1])

# Q7: Print every 2nd character of 'word' starting from index 0.
# Your code here:
print(word[::2])


# ==========================================
# 3. STRING METHODS (CASE CONVERSION)
# ==========================================

sentence = "hello WORLD from python"

# Q8: Convert 'sentence' to all uppercase.
# Your code here:
print(sentence.upper())

# Q9: Convert 'sentence' to all lowercase.
# Your code here:
print(sentence.lower())

# Q10: Convert 'sentence' to Title Case (Capitalize first letter of each word).
# Your code here:
print(sentence.title())

# Q11: Swap the case of 'sentence' (uppercase becomes lowercase & vice versa).
# Your code here:
print(sentence.swapcase())

# ==========================================
# 4. SEARCHING & COUNTING
# ==========================================

quote = "Learning Python is fun. Python is powerful!"

# Q12: Count how many times the word "Python" appears in 'quote'.
# Your code here:
print(quote.count("Python"))

# Q13: Find the starting index position of the word "fun" in 'quote'.
# Your code here:
print(quote.find("fun"))

# Q14: Check if 'quote' starts with the word "Learning" (returns True/False).
# Your code here:
print(quote.startswith("Learning"))

# Q15: Check if 'quote' ends with an exclamation mark "!" (returns True/False).
# Your code here:
print(quote.endswith("!"))

# ==========================================
# 5. STRING MODIFICATION & REPLACEMENT
# ==========================================

raw_text = "   too much whitespace   "

# Q16: Remove leading and trailing spaces from 'raw_text'.
# Your code here:
print(raw_text.strip())

# Q17: Replace the word "fun" with "awesome" in 'quote' (from Q12).
# Your code here:
print(quote.replace("fun", "awesome"))

# ==========================================
# 6. SPLITTING & JOINING
# ==========================================

csv_line = "apple,banana,cherry,dragonfruit"

# Q18: Split 'csv_line' by commas into a list of fruits.
# Your code here:
print(csv_line.split(","))

# Q19: Join a list of words into a single string separated by spaces.
words_list = ["Python", "is", "very", "easy"]
# Your code here:
print(" ".join(words_list))

# ==========================================
# 7. STRING FORMATTING (f-strings)
# ==========================================

name = "Abhay"
age = 20

# Q20: Use an f-string to print: "My name is Abhay and I am 20 years old."
# Your code here:
print(f"My name is {name} and I am {age} years old.")

# ==========================================
# 8. STRING CHECKING & INSPECTION
# ==========================================

num_str = "12345"
alpha_str = "Python"

# Q21: Check if 'num_str' contains only digits (returns True/False).
# Your code here:
print(num_str.isdigit())

# Q22: Check if 'alpha_str' contains only alphabetic characters (returns True/False).
# Your code here:
print(alpha_str.isalpha())

# ==========================================
# 9. MINI CHALLENGES
# ==========================================

# Q23: Count the total number of vowels (a, e, i, o, u) in the string below.
sample_str = "Artificial Intelligence"
# Your code here:
vowels = "aeiouAEIOU"
count = 0
for char in sample_str:
    if char in vowels:
        count += 1
print("Vowel count:", count)

# Q24: Check if the string below is a Palindrome (reads same forwards and backwards).
test_palindrome = "radar"
# Your code here:
print(test_palindrome == test_palindrome[::-1])

