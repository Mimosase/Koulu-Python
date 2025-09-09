def gallons_to_liters(amount_gal):
    return amount_gal * 3.785

while True:
    amount_gal = float(input("Enter a volume in American gallons (negative value to quit): "))
    if amount_gal < 0:
        break

    amount_lit = gallons_to_liters(amount_gal)
    print(f"{amount_gal} American gallons is {amount_lit:.2f} liters.")

print("Program finished.")