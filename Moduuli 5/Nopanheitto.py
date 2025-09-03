import random
total_dicerolls = []
rolls = int(input("How many dice to roll:"))

for dicerolls in range(rolls):
    total_dicerolls.append(random.randint(1,6))
dice_sum = sum(total_dicerolls)
print(f"Sum of the dice: {dice_sum}")