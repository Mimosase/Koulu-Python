amount_gal = float(input("Enter a volume in American gallons (negative value to quit):"))

def gas(amount_gal):
    liter = amount_gal * 3.785
    return liter

print(gas(amount_gal))