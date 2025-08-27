while True:
    number = float(input("Enter length in inches (negative value to quit): "))
    tulos = number * 2.54
    if number >= 0:
        print(f"{number} inches is {tulos:.2f} centimeters")
    else:
        break

print("Program ended.")