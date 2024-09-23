def pesquisa_sequencial_modificada(lista, alvo):
    # Percorre cada elemento na lista até encontrar o alvo ou um elemento maior
    for elemento in lista:
        if elemento == alvo:
            return True  # Melhor caso: O(1)
        elif elemento > alvo:
            return False  # Interrompe a busca
    return False  # Pior caso: O(n)

# Complexidade:
# Melhor Caso: O(1) - Alvo encontrado na primeira posição
# Pior Caso: O(n) - Alvo não encontrado ou no final da lista
# Caso Médio: O(n) - Em média, percorre metade da lista
