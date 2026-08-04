"""
05. String Manipulation - Code Examples
---------------------------------------
Demonstrates indexing, step slicing, string methods, palindrome checks, and vowel counting.
"""

# 1. Reverse Slicing & Step Slicing
text = "Python Programming"
print("Original:", text)
print("Reversed:", text[::-1])
print("Every 2nd char:", text[::2])

# 2. String Cleaning, Replacement & Splitting
raw_csv = "  apple , banana , cherry , date  "
cleaned_list = [item.strip() for item in raw_csv.split(",")]
print("\nCleaned CSV items:", cleaned_list)

rejoined_text = " | ".join(cleaned_list)
print("Rejoined String:", rejoined_text)

# 3. Palindrome Check Function
def is_palindrome(s: str) -> bool:
    cleaned = "".join(ch.lower() for ch in s if ch.isalnum())
    return cleaned == cleaned[::-1]

print("\n=== Palindrome Checks ===")
print("'radar' is palindrome?", is_palindrome("radar"))
print("'A man, a plan, a canal: Panama' is palindrome?", is_palindrome("A man, a plan, a canal: Panama"))

# 4. Vowel Frequency Counter
phrase = "Artificial Intelligence"
vowels = "aeiou"
freq = {v: phrase.lower().count(v) for v in vowels if phrase.lower().count(v) > 0}
print("\nVowel Frequencies:", freq)
