print("Hei keskiajalle jäänyt kaveri! Muunnetaan antiikkiset mittasi nykyäjan mittoihin.")
print("Syötä massa leivisköinä, nauloina ja luoteina.")

amount_le = int(input("Leiviskät:"))
amount_na = int(input("Naulat:"))
amount_lu = float(input("Luodit:"))

luoti = 13,3
naula = 32 * luoti
leiviskä = 20 * naula

print((luoti*amount_lu) + (naula * amount_na) + (leiviskä*amount_le))