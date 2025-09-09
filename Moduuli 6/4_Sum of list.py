#Kirjoita funktio nimeltä sum_of_list, joka saa parametrina kokonaislukuja sisältävän listan.
# Funktio palauttaa listassa olevien lukujen summan. Kirjoita testausta varten pääohjelma,
# jossa luot listan, kutsut funktiota ja tulostat sen palauttaman arvon.

lista = [5,5,5]

def sum_of_list(lista):
    return sum(lista)

print(f"The sum of the numbers in the list is: {sum(lista)}")