# Question: Create a record of a theatre using a Python dictionary:
# - Add theatre name
# - Add movie name
# - Add hero name
# - Add heroine name
# - Add director name

# Approach 1: Single Record Dictionary
theatre_record = {
    "theatre_name": "PVR ICON IMAX",
    "movie_name": "Spider-Man: Brand New Day",
    "hero_name": "Tom Holland",
    "heroine_name": "Zendaya",
    "director_name": "Destin Daniel Cretton"
}

print("1. Single Record Dictionary:")
print(theatre_record)

print("\n" + "="*60 + "\n")

# Approach 2: Multiple Records Dictionary (Lists as Values)
movies_record = {
    "t name": ["pvr", "inox", "city pride", "ashok"],
    "movie name": ["pushpa", "raja shivchhatrapati", "chhava", "thor"],
    "hero": ["allu arjun", "sharad kelkar", "vicky kaushal", "chris hemsworth"],
    "heroine": ["rashmika", "mrunal thakur", "rashmika", "natalie portman"],
    "director": ["sukumar", "digpal lanjekar", "laxman uttekar", "taika waititi"]
}

print("2. Multiple Records Dictionary (Lists as Values):")
print(movies_record)
