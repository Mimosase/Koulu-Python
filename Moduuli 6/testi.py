

lista = [2,3,4,5,6]

def filter_even_numbers(lista):
    even_list = []

    #joka kerta kun for-looppi on käyty läpi "luku" muuttuja nousee 0->1->2...
    for luku in lista:

        if luku % 2 == 0:
            even_list.append(luku)

    return even_list



print(filter_even_numbers(lista))


