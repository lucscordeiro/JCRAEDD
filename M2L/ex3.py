def expo(base, expoente):
    resultado = 1
    # Itera expoente vezes para multiplicar a base
    for _ in range(expoente):
        resultado *= base  # Operação constante
    return resultado

# Complexidade:
# Tempo: O(e) - Onde e é o expoente, pois realiza e multiplicações
# Espaço: O(1) - Utiliza espaço constante para variáveis
