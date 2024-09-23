def verificar_ordenado(vetor):
    n = len(vetor)
    # Percorre o vetor a partir do segundo elemento
    for i in range(1, n):
        if vetor[i] < vetor[i - 1]:
            return  # Não está ordenado
    print("ORDENADO")  # Todos os elementos estão em ordem crescente

# Complexidade:
# Melhor Caso: O(1) - Vetor não está ordenado logo na primeira comparação
# Pior Caso: O(n) - Vetor está ordenado ou a violação ocorre no final
# Espaço: O(1) - Utiliza espaço constante
