# Question:
# 1. Create a record for real estate clients or real estate builders
#    - Add site name
#    - Available flats
#    - Add amt of flats
# 2. Add 4 BHK flat after creation of record (location of 4 BHK is after 2 BHK)
# 3. Remove 1 BHK flat because it is sold
# 4. Update necessary another columns and records according to the condition
# 5. Sort site records in ascending order and price record in descending order

real_estate = {
    "site": ["Skyline", "Green Acres", "Amanora", "Blue Ridge"],
    "flats": ["1bhk", "2bhk", "3bhk"],
    "amt": [4500000, 7500000, 11000000]
}
print("Records:", real_estate)

i = real_estate["flats"].index("2bhk")
real_estate["flats"].insert(i + 1, "4bhk")
real_estate["amt"].insert(i + 1, 16000000)
print("\nAfter Adding 4bhk:", real_estate)

i = real_estate["flats"].index("1bhk")
rem_flat = real_estate["flats"].pop(i)
rem_amt = real_estate["amt"].pop(i)
print(f"\nSold Flat Removed: {rem_flat} (Price: {rem_amt})")
print("After Removing 1bhk:", real_estate)

real_estate["site"].sort()
real_estate["amt"].sort(reverse=True)

print("\nSites Ascending:", real_estate["site"])
print("Prices Descending:", real_estate["amt"])
