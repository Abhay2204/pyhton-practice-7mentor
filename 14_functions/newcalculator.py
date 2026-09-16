"""
Interactive Terminal Calculator
Consumes functions from process.py to demonstrate modular programming.
"""

from process import add, sub, multiplication, division, modulus, power

def run_calculator():
    """Main calculator loop."""
    print("=" * 45)
    print("   🧮 Modular Python Calculator (Functions)")
    print("=" * 45)

    while True:
        print("\nOperations:")
        print("  1. Add (+)")
        print("  2. Subtract (-)")
        print("  3. Multiply (*)")
        print("  4. Divide (/)")
        print("  5. Modulus (%)")
        print("  6. Power (^)")
        print("  7. Exit")

        try:
            choice = int(input("\nEnter choice (1-7): ").strip())
        except ValueError:
            print("❌ Invalid input! Please enter a number between 1 and 7.")
            continue

        if choice == 7:
            print("\nCalculator closed. Have a great day!")
            break

        if choice in (1, 2, 3, 4, 5, 6):
            try:
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
            except ValueError:
                print("❌ Please enter valid numerical values.")
                continue

            if choice == 1:
                print(f"👉 Result: {a} + {b} = {add(a, b)}")
            elif choice == 2:
                print(f"👉 Result: {a} - {b} = {sub(a, b)}")
            elif choice == 3:
                print(f"👉 Result: {a} * {b} = {multiplication(a, b)}")
            elif choice == 4:
                res = division(a, b)
                print(f"👉 Result: {a} / {b} = {res}")
            elif choice == 5:
                res = modulus(a, b)
                print(f"👉 Result: {a} % {b} = {res}")
            elif choice == 6:
                print(f"👉 Result: {a} ^ {b} = {power(a, b)}")
        else:
            print("❌ Invalid choice. Please choose from 1 to 7.")

if __name__ == "__main__":
    run_calculator()
