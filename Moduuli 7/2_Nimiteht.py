names = set()
while True:
    name = input("Enter a name")

    if name in names:
        print("Existing name")

    elif name == "":
        break

    else:
        names.add(name)
        print("New name")

for n in names:
    print(n)