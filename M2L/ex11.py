def fragmento_dois_loops(n):
    s = 0
    # Primeiro loop: O(n)
    for i in range(n - 1):
        # Segundo loop: O(n) - Vai de 1 até 2n, mas 2n é constante proporcional a n
        for j in range(1, 2 * n):
            s += 1  # Operação constante
    return s

# Complexidade:
# Tempo: O(n^2) - Dois loops aninhados, cada um iterando proporcionalmente a n vezes
# Espaço: O(1) - Utiliza espaço constante para a variável s
