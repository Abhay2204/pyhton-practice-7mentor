# ❓ 10. Real-World Mini-Projects - Questions & Challenges

## 📝 Problem Statements & Exercises

### Challenge 1: E-Commerce Inventory Stock Sync
Given vendor catalog `catalog = {"Laptop": 10, "Phone": 25, "Headphones": 15}` and customer cart `cart = ["Laptop", "Phone", "Phone"]`, write a function to update the inventory stock and calculate order total given prices `prices = {"Laptop": 1000, "Phone": 500, "Headphones": 100}`.

**Solution:**
```python
catalog = {"Laptop": 10, "Phone": 25, "Headphones": 15}
prices = {"Laptop": 1000, "Phone": 500, "Headphones": 100}
cart = ["Laptop", "Phone", "Phone"]

total_cost = 0
for item in cart:
    if catalog.get(item, 0) > 0:
        catalog[item] -= 1
        total_cost += prices[item]

print("Updated Catalog:", catalog)
print("Total Order Cost: $", total_cost)
```
