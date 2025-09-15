 #Kirjoita funktio nimeltä calculate_unit_price, joka saa parametreina pyöreän pizzan halkaisijan
 #senttimetreinä ja pizzan hinnan euroina. Funktio laskee ja palauttaa pizzan yksikköhinnan euroina per neliömetri.
 #Pääohjelma kysyy käyttäjältä kahden pizzan halkaisijat ja hinnat sekä ilmoittaa,
 #kumpi pizza antaa paremman vastineen rahalle (eli kummalla on alhaisempi yksikköhinta).
 #Yksikköhintojen laskennassa on käytettävä kirjoittamaasi calculate_unit_price-funktiota.

import math

# Ympyrän pinta-ala lasketaan kaavalla A = πr², missä r on ympyrän säde.

def calculate_unit_price(halkaisija,hinta):
    pinta_ala = halkaisija ** 2 * math.pi
    yksikkohinta =  hinta / pinta_ala
    return yksikkohinta

halkaisija = float(input("Enter the diameter of the first pizza (cm): "))
hinta = float(input("Enter the price of the first pizza (euros):"))

calculate_unit_price(halkaisija,hinta)
