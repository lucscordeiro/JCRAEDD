def tem_duplicacao(array, n):
    # Percorre cada elemento do array
    for i in range(n):
        val = array[i]
        # Verifica se há duplicação nos elementos seguintes
        for j in range(i + 1, n):
            if array[j] == val:
                return True  # Retorna imediatamente se encontrar duplicação
    return False  # Nenhuma duplicação encontrada

# Complexidade:
# Melhor Caso: O(1) - Duplicação encontrada na primeira comparação
# Pior Caso: O(n^2) - Nenhuma duplicação ou duplicação no final do array
# Caso Médio: O(n^2) - Comparações proporcionais a n*(n-1)/2
