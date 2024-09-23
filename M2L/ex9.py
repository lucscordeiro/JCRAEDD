def multiplicar_matrizes(A, B, n):
    # Inicializa a matriz resultado com zeros
    mat = [[0 for _ in range(n)] for _ in range(n)]
    
    # Percorre cada linha de A
    for i in range(n):  # O(n)
        # Percorre cada coluna de B
        for j in range(n):  # O(n)
            mat[i][j] = 0  # Inicialização (operação constante)
            # Multiplica elementos correspondentes e soma
            for k in range(n):  # O(n)
                mat[i][j] += A[i][k] * B[k][j]  # Operação constante
    return mat

# Complexidade:
# Tempo: O(n^3) - Três loops aninhados, cada um iterando n vezes
# Espaço: O(n^2) - Armazenamento das matrizes A, B e mat
