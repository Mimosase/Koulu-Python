#Kirjoita funktio nimeltä filter_even_numbers, joka saa parametrina kokonaislukuja sisältävän listan.
#Funktio palauttaa toisen listan, joka on muuten sama kuin alkuperäinen,
# mutta kaikki parittomat luvut on poistettu. Testausta varten kirjoita pääohjelma,
# jossa luot listan, kutsut funktiota, ja tulostat sekä alkuperäisen että karsitun listan.

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def filter_even_numbers(lista):
    even_list = []

    #luku = 0->1->2...
    for luku in range(len(lista)):

        if lista[luku] % 2 == 0:
            even_list.append(lista[luku])

    return even_list

print(f"Original list: {lista}")
print(f"List with even numbers only: {filter_even_numbers(lista)}")


