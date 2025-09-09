# Kirjoita funktio nimeltä roll_dice, joka palauttaa satunnaisen nopan silmäluvun väliltä 1..6.
# Funktiolla ei ole parametreja. Kirjoita pääohjelma, joka heittää noppaa, kunnes tulee 6.
# Pääohjelma tulostaa kunkin heiton jälkeen saadun silmäluvun.

import random
def roll_dice():
    roll = 0
    while roll != 6:
        roll = random.randint(1,6)
        print(roll)
        if roll == 6:
            break

roll_dice()