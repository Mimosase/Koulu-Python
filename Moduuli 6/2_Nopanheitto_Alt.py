import random
sides = int(input("How many sides on dice"))
def roll_dice(sides):
    return random.randint(1,sides)

diceroll = roll_dice(sides)
while diceroll != sides:
    print(diceroll)
    diceroll = roll_dice(sides)

print(diceroll)

