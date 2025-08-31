import random
real_number = random.randint(1, 10)

while True:
    guess = int(input("Guess a number (1-10): "))

    if guess == real_number:
        break

    elif guess > real_number:
        print("Too high")

    elif guess < real_number:
        print("Too low")

print("Correct")