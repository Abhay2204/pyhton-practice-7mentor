# Question:
# Create a dictionary of 5 states with cities for each state.
# Update the state 'Maharashtra' by adding the new city 'Palghar' and removing 'Pune'.

state_cities = {
    "Maharashtra": ["Mumbai", "Pune", "Nagpur", "Nashik"],
    "Gujarat": ["Ahmedabad", "Surat", "Vadodara", "Rajkot"],
    "Rajasthan": ["Jaipur", "Udaipur", "Jodhpur", "Kota"],
    "Karnataka": ["Bengaluru", "Mysuru", "Hubballi", "Mangaluru"],
    "Tamil Nadu": ["Chennai", "Coimbatore", "Madurai", "Salem"]
}

state_cities["Maharashtra"].append("Palghar")
state_cities["Maharashtra"].remove("Pune")

print(state_cities)
