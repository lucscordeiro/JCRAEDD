def inserir_numero(vetor, numero):
    n = len(vetor)
    # Busca binária para encontrar a posição correta de inserção
    esquerda = 0
    direita = n - 1
    pos = n  # Posição padrão se o número for maior que todos os elementos

    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if vetor[meio] >= numero:
            pos = meio
            direita = meio - 1
        else:
            esquerda = meio + 1

    # Desloca os elementos para a direita a partir da posição encontrada
    vetor.append(0)  # Aumenta o tamanho do vetor
    for i in range(n, pos, -1):
        vetor[i] = vetor[i - 1]  # Deslocamento, operação constante

    vetor[pos] = numero  # Insere o número na posição correta
    return vetor

# Complexidade:
# Tempo:
# - Busca binária: O(log n)
# - Deslocamento dos elementos: O(n) no pior caso (inserção no início)
# - Total:
#   - Melhor Caso: O(log n) + O(1) = O(log n) (inserção no final)
#   - Pior Caso: O(log n) + O(n) = O(n)
# Espaço:
# - O(1) adicional além do vetor, mas o vetor pode aumentar seu tamanho
