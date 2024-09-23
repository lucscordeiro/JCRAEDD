def expo(base, expoente):
    if expoente == 0:
        return 1  # Caso base
    elif expoente % 2 == 1:
        return base * expo(base, expoente - 1)  # Reduz o expoente linearmente
    else:
        meio = expo(base, expoente // 2)  # Divide o expoente pela metade
        return meio * meio  # Multiplica o resultado da metade

# Complexidade:
# Tempo: O(log e) - Divide o problema pela metade a cada chamada recursiva
# Espaço: O(log e) - Espaço na pilha de chamadas recursivas proporcional a log e
