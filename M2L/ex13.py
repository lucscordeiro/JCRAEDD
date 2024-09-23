def fragmento_dois_loops_aninhados(V, n):
    # Percorre elementos com passo 2
    for i in range(0, n, 2):  # Aproximadamente n/2 iterações, O(n)
        # Percorre de n até 0, decrementando
        for j in range(n, -1, -1):  # n+1 iterações, O(n)
            if V[i] < V[j]:
                print(i)  # Operação constante

# Complexidade:
# Tempo: O(n^2) - Dois loops aninhados, cada um iterando proporcionalmente a n vezes
# Espaço: O(1) - Utiliza espaço constante
