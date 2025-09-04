kaupungit = []

for luku in range(0, 5):
    kaupunki = input("Enter the name of a city: ")
    kaupungit.append(kaupunki)

print("\n")
print("The cities you entered: ")
for luku in kaupungit:
    print(luku)