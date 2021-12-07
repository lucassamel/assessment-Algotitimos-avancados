def divideLista(lista, primeiro, ultimo, inicio, meio):
    pivo = lista[ultimo]
    fim = ultimo

    while (meio[0] <= fim):
        if (lista[meio[0]] < pivo):
            lista[meio[0]], lista[inicio[0]] = lista[inicio[0]], lista[meio[0]]
            meio[0] = meio[0] + 1
            inicio[0] = inicio[0] + 1
        elif (lista[meio[0]] > pivo):
            lista[meio[0]], lista[fim] = lista[fim], lista[meio[0]]
            fim = fim - 1
        else:
            meio[0] = meio[0] + 1


def quicksort(lista, primeiro, ultimo):

    if (primeiro >= ultimo):
        return
    if (ultimo == primeiro + 1):
        if (lista[primeiro] > lista[ultimo]):
            lista[primeiro], lista[ultimo] = lista[ultimo], lista[primeiro]
            return


    inicio = [primeiro]
    meio = [primeiro]
    divideLista(lista, primeiro, ultimo, inicio, meio)
    quicksort(lista, primeiro, inicio[0] - 1)
    quicksort(lista, meio[0], ultimo)


lista = [7,6,6,5,5,5,1,1,1,3,3,3,9,9,8,8,4,4,4,3,3]
quicksort(lista, 0, len(lista) - 1)
print(lista)
