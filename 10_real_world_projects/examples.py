"""
10. Real-World Mini-Projects & Scenarios - Code Examples
---------------------------------------------------------
Consolidates real-world mini-projects covering inventory, roll tracking, and college grade mapping.
"""

print("=== 1. Newspaper Seller Inventory ===")
newspapers = ["Times of India", "Hindustan Times", "Dainik Bhaskar", "The Indian Express", "Navbharat Times"]
print("Seller Stock:", newspapers)

buyer_basket = newspapers.copy()
buyer_basket.remove("Times of India")
print("Buyer Basket after purchase:", buyer_basket)
print("Seller Stock (Unchanged):", newspapers)


print("\n=== 2. School Roll Number Management ===")
rolls = set(range(1, 61))
rolls.remove(35) # Student left school
print("Total Active Roll Numbers:", len(rolls))
print("Sorted Roll Numbers (First 10):", sorted(rolls)[:10])


print("\n=== 3. Pune Colleges NAAC Grade Mapping ===")
colleges = ["COEP", "MIT", "DY Patil", "PICT", "VIT"]
idx_dy = colleges.index("DY Patil")
colleges.pop(idx_dy)

idx_mit = colleges.index("MIT")
colleges.insert(idx_mit + 1, "ASM CSIT")

grades = ["A++", "A+", "A", "A+", "A+"]
college_record = dict(zip(colleges, grades))
print("College Grade Mapping:", college_record)
