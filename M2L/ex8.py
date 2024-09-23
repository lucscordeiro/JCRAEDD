def ache_min(array, n):
    min_val = array[0]
    # Percorre todos os elementos para encontrar o mínimo
    for i in range(1, n):
        if array[i] < min_val:
            min_val = array[i]
    return min_val

# Complexidade:
# Tempo: O(n) - Necessita verificar cada elemento uma vez
# Espaço: O(1) - Utiliza espaço constante para armazenar min_val
