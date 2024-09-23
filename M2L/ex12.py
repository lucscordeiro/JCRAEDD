for i in range(n):
    print(i)  # Operação constante

# Complexidade:
# Tempo: O(n) - Executa n iterações
# Espaço: O(1) - Utiliza espaço constante


for i in range(0, n, 2):
    print(i)  # Operação constante

# Complexidade:
# Tempo: O(n) - Executa aproximadamente n/2 iterações, ainda proporcional a n
# Espaço: O(1) - Utiliza espaço constante


for i in range(0, n, 2):
    print(i)  # Operação constante
    i -= 1  # Não afeta o loop em Python

# Complexidade:
# Tempo: O(n) - Executa aproximadamente n/2 iterações, ainda proporcional a n
# Espaço: O(1) - Utiliza espaço constante
