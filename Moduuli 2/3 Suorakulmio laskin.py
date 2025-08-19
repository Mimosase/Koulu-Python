print("Tämä on suorakulmiolaskin! Kerro minulle kanta ja korkeus, niin lasken sinulle suorakulmion piirin ja pinta- alan.")
kanta = int(input("Kanta:"))
korkeus = int(input("Korkeus:"))

print("Piiri:", (kanta + kanta + korkeus + korkeus), "yksikköä")
print("Pinta- ala", (kanta * korkeus), "yksikköä")