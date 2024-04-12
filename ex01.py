lista = [5, 7, 3, 6]
lista.cont(0)
pos = 2
for i in range(len(lista)-1, pos-1, -1):
    lista[i] = lista[i-1]
    lista[pos] = 8
    print('lista')