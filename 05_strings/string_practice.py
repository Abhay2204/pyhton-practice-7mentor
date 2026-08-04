"""
Python String Practice Questions
--------------------------------
This file contains various basic-to-intermediate string practice questions 
covering indexing, slicing, case conversions, searching, modification, 
splitting, joining, f-strings, and algorithms.
"""

# ==========================================
# 1. STRING CREATION & INDEXING
# ==========================================

text = "Python Programming"
print("First character:", text[0])
print("Last character:", text[-1])
print("Character at index 7:", text[7])
print("3rd character from end:", text[-3])


# ==========================================
# 2. STRING SLICING
# ==========================================

word = "Antigravity"
print("First 4 chars:", word[:4])
print("From index 4 to end:", word[4:])
print("Reversed word:", word[::-1])
print("Every 2nd char:", word[::2])


# ==========================================
# 3. STRING METHODS (CASE CONVERSION)
# ==========================================

sentence = "hello WORLD from python"
print("Uppercase:", sentence.upper())
print("Lowercase:", sentence.lower())
print("Title Case:", sentence.title())
print("Swap Case:", sentence.swapcase())


# ==========================================
# 4. SEARCHING & COUNTING
# ==========================================

quote = "Learning Python is fun. Python is powerful!"
print("Count of 'Python':", quote.count("Python"))
print("Index of 'fun':", quote.find("fun"))
print("Starts with 'Learning':", quote.startswith("Learning"))
print("Ends with '!':", quote.endswith("!"))


# ==========================================
# 5. STRING MODIFICATION & REPLACEMENT
# ==========================================

raw_text = "   too much whitespace   "
print("Stripped text:", raw_text.strip())
print("Replaced 'fun' with 'awesome':", quote.replace("fun", "awesome"))


# ==========================================
# 6. SPLITTING & JOINING
# ==========================================

csv_line = "apple,banana,cherry,dragonfruit"
fruits_list = csv_line.split(",")
print("Split list:", fruits_list)

words_list = ["Python", "is", "very", "easy"]
print("Joined string:", " ".join(words_list))


# ==========================================
# 7. STRING FORMATTING (f-strings)
# ==========================================

name = "Abhay"
age = 20
print(f"My name is {name} and I am {age} years old.")


# ==========================================
# 8. STRING CHECKING & INSPECTION
# ==========================================

num_str = "12345"
alpha_str = "Python"
print("num_str.isdigit():", num_str.isdigit())
print("alpha_str.isalpha():", alpha_str.isalpha())


# ==========================================
# 9. MINI CHALLENGES
# ==========================================

sample_str = "Artificial Intelligence"
vowels = "aeiouAEIOU"
count = sum(1 for char in sample_str if char in vowels)
print("Vowel count:", count)

test_palindrome = "radar"
print(f"Is '{test_palindrome}' palindrome?", test_palindrome == test_palindrome[::-1])
