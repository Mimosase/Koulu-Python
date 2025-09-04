number = int(input("Enter an integer: "))

if number > 1:
    for numbers in range(2, number):
        if number % numbers == 0:
            print(f"{number} is not a prime number.")
            break
    else:
        print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")
