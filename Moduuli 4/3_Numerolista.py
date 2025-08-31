numbers = []

while True:
    number = input("Enter a number (or press Enter to quit): ")

    if number == "":
        break

    number = float(number)
    numbers.append(number)

numbers.sort()
print(f"Smallest number: {(numbers[0])}\nLargest number: {(numbers[-1])}")
