numbers = []

number = input("Enter a number: ")

while number != "":
    number = float(number)
    numbers.append(number)
    number = input("Enter a number: ")

numbers.sort(reverse=True)
print("The greatest numbers in descending order: ")
for i in range(0,min(5,len(numbers))):
    print(numbers[i])