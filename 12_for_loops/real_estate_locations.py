"""
Real Estate Record - Print All Locations Using For Loop
-------------------------------------------------------
Question:
1. Create a record for Real Estate:
   - Add company name
   - Location
   - Flats
2. Use a for loop to print all locations from the record.
"""

# ==========================================
# APPROACH 1: Single Record with Multiple Locations (Dictionary with Lists)
# ==========================================
real_estate = {
    "company_name": "Godrej Properties",
    "location": ["Kharadi", "Hinjewadi", "Baner", "Wakad", "Hadapsar"],
    "flats": ["1 BHK", "2 BHK", "3 BHK", "4 BHK"]
}

print("=== All Locations (Approach 1) ===")
for loc in real_estate["location"]:
    print(f"Location: {loc}")
print()


# ==========================================
# APPROACH 2: Multiple Real Estate Projects (List of Dictionaries)
# ==========================================
projects = [
    {"company_name": "Godrej Properties", "location": "Kharadi", "flats": "2 BHK, 3 BHK"},
    {"company_name": "Kolte Patil", "location": "Hinjewadi", "flats": "1 BHK, 2 BHK"},
    {"company_name": "VTP Realty", "location": "Baner", "flats": "2 BHK, 3 BHK, 4 BHK"},
    {"company_name": "Amanora Park Town", "location": "Hadapsar", "flats": "1 BHK, 2 BHK"}
]

print("=== All Locations (Approach 2: List of Records) ===")
for project in projects:
    print(f"Company: {project['company_name']:20} | Location: {project['location']}")
