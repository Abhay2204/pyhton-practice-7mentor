hero = {
    "name": ["abhay", "anuj", "ajay"],
    "movie": ["bbch", "pathaan", "jawan"]
}
print("Original dictionary:")
print(hero)

# Updating the 3rd movie (index 2) to "pk"
hero["movie"][2] = "pk"
print("\nAfter updating index 2:")
print(hero)

# Inserting a new movie at a specific position (e.g. index 1) using .insert(index, value)
hero["movie"].insert(1, "dangal")
print("\nAfter inserting 'dangal' at index 1:")
print(hero)

# Sorting the movies list in alphabetical order
hero["movie"].sort()
print("\nAfter sorting movies:")
print(hero)