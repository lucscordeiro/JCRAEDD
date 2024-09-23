def reverse(lista):
    n = len(lista)
    # Itera apenas até a metade da lista
    for i in range(n // 2):
        # Troca o elemento na posição i com o elemento na posição n-1-i
        lista[i], lista[n - 1 - i] = lista[n - 1 - i], lista[i]
    return lista

# Complexidade:
# Tempo: O(n) - Necessita percorrer metade da lista, proporcional a n
# Espaço: O(1) - Inversão realizada in-place, sem espaço adicional significativo
