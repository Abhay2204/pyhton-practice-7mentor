constituency_mla = {
    "Chinchwad": "Ashwini Jagtap",
    "Kothrud": "Chandrakant Patil",
    "Shivajinagar": "Siddharth Shirole",
    "Kasba Peth": "Ravindra Dhangekar",
    "Hadapsar": "Chetan Tupe"
}


print(constituency_mla)

removed_mla = constituency_mla.pop("Chinchwad")

print("Removed MLA from Chinchwad:", removed_mla)

print("Updated Constituency & MLA Record:")
print(constituency_mla)
