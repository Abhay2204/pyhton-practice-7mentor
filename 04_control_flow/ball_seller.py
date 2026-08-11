price = int(input("Enter your price range: "))

if 1000 <= price < 20000:
    print("Red ball")
elif 20000 <= price < 30000:
    print("Green ball")
elif price >= 30000:
    print("Yellow ball")
else:
    print("Bye bye")
