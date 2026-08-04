"""
08. Set Theory & Operations - Code Examples
--------------------------------------------
Demonstrates mathematical set operations, frozenset usage, and discard vs remove.
"""

set_A = {1, 2, 3, 4, 5}
set_B = {4, 5, 6, 7, 8}

print("=== Set Operations ===")
print("Set A:", set_A)
print("Set B:", set_B)

print("\nUnion (A | B):", set_A | set_B)
print("Intersection (A & B):", set_A & set_B)
print("Difference (A - B):", set_A - set_B)
print("Symmetric Difference (A ^ B):", set_A ^ set_B)

# Frozenset Demo
fz = frozenset([1, 2, 3, 4])
print("\n=== Frozenset ===")
print("Frozenset:", fz)
# Dict key using frozenset:
dataset = {fz: "Immutable Set Data"}
print("Frozenset as Dict Key:", dataset[fz])
