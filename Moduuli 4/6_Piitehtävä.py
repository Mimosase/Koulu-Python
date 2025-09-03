import random

amount = int(input("Syötä pisteiden määrä: "))

# piirretyt pisteet ympyrän sisälle/ ulkopuolelle yhteensä
total_amount_of_dots = 0
# ympyrän sisälle piirettävät pisteet
inside_the_circle = 0

while total_amount_of_dots < amount:
    # random.uniform palauttaa satunnaisen FLOAT numeron numeron -1 ja 1 välillä
    a = random.uniform(-1, 1)
    b = random.uniform(-1, 1)
    # 2 kertomerkkiä ** = potenssi
    # piirretään neliö
    if a ** 2 + b ** 2 < 1:
        inside_the_circle += 1
    total_amount_of_dots += 1

approxmated_pie = 4 * inside_the_circle / amount

print(f"Approximation of pi: {approxmated_pie}")
