# Maharashtra Assembly Election Eligibility Checker
# Logic: Candidate must have property >= 150 rs AND be qualified

def check_election_eligibility():
    print("=" * 45)
    print("  Maharashtra Assembly Election Checker")
    print("=" * 45)
    print()

    # Input: Property value
    try:
        property_value = float(input("Enter your property value (in rs): "))
    except ValueError:
        print("Invalid input! Please enter a numeric value.")
        return

    # Input: Qualification status
    qualified_input = input("Are you qualified? (yes/no): ").strip().lower()

    if qualified_input in ("yes", "y"):
        is_qualified = True
    elif qualified_input in ("no", "n"):
        is_qualified = False
    else:
        print("Invalid input! Please enter 'yes' or 'no'.")
        return

    print()
    print("-" * 45)

    # Election eligibility logic
    has_property = property_value >= 150

    if has_property and is_qualified:
        print("✅ You are ELIGIBLE for the election!")
    else:
        print("❌ You are NOT ELIGIBLE for the election.")
        if not has_property:
            print("   Reason: Property value must be at least 150 rs.")
        if not is_qualified:
            print("   Reason: You must be qualified.")

    print("-" * 45)


# Run the program
check_election_eligibility()
