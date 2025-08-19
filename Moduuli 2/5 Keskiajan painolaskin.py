talents = float(input("Enter talents: "))
pounds = float(input("Enter pounds: "))
lots = float(input("Enter lots: "))

luoti = 13.3
naula = 32 * luoti
leiviskä = 20 * naula

total_grams = (luoti*lots) + (naula * pounds) + (leiviskä*talents)
kilograms = total_grams // 1000
remaining_grams = total_grams % 1000

print("The weight in modern units:")
print(f"{int(kilograms)} kilograms and {remaining_grams:.2f} grams.")