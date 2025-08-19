print("Hei keskiajalle jäänyt kaveri! Muunnetaan antiikkiset mittasi nykyäjan mittoihin.")
print("Syötä massa leivisköinä, nauloina ja luoteina.")

amount_le = float(input("Leiviskät:"))
amount_na = float(input("Naulat:"))
amount_lu = float(input("Luodit:"))

luoti = 13.3
naula = 32 * luoti
leiviskä = 20 * naula

tulos = (luoti*amount_lu) + (naula * amount_na) + (leiviskä*amount_le)
tulos_kiloissa = tulos // 1000
tulos_grammoissa = tulos % 1000

print(f"{tulos_kiloissa} kiloa ja {tulos_grammoissa:.2f} grammaa.")