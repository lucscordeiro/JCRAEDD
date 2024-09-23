def fragmento_tres_loops(n):
    s = 0
    # Primeiro loop: O(n)
    for i in range(n - 1):
        # Segundo loop: O(n) no pior caso (j vai de i+1 até n-1)
        for j in range(i + 1, n):
            # Terceiro loop: O(j) no pior caso (k vai de 1 até j-1)
            for k in range(1, j):
                s = 1  # Operação constante
    return s

# Complexidade:
# Tempo: O(n^3) - Três loops aninhados, com a complexidade total proporcional a n^3
# Espaço: O(1) - Utiliza espaço constante para a variável s
