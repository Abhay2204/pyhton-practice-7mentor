age = int(input("Enter age: "))

if age >= 18:
    card = input("Do you have voting card (yes/no): ").lower()
    if card == "yes":
        print("ready to vote")
    else:
        print("not ready to vote")
else:
    print("you are child")
