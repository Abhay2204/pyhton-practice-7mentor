# Question: Create a record of a theatre using a Python dictionary:
# - Add theatre name
# - Add movie name
# - Add hero name
# - Add heroine name
# - Add director name

theatre_record = {
    "theatre_name": "PVR ICON IMAX",
    "movie_name": "Spider-Man: Brand New Day",
    "hero_name": "Tom Holland",
    "heroine_name": "Zendaya",
    "director_name": "Destin Daniel Cretton"
}

print("+" + "-" * 20 + "+" + "-" * 27 + "+")
print(f"| {'FIELD':<18} | {'DETAILS':<25} |")
print("+" + "-" * 20 + "+" + "-" * 27 + "+")

for key, value in theatre_record.items():
    field_name = key.replace("_", " ").title()
    print(f"| {field_name:<18} | {value:<25} |")

print("+" + "-" * 20 + "+" + "-" * 27 + "+")
