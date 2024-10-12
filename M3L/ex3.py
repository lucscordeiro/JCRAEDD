"""
3. Um vetor de tamanho n, pode conter elementos do alfabeto e numerais 0 a 9. 
Escreva um algoritmo que seja capaz de localizar, pelo método binário, um caractere 
fornecido pelo usuário. Se esse caractere for uma letra, o usuário poderá fornecê-la 
para a busca no formato maiúsculo ou minúsculo.
"""


def pesquisa_binaria(vetor, valor):
    # Converte todos os caracteres para maiúsculas para unificar a busca
    valor = valor.upper()
    vetor = [str(item).upper() for item in vetor]  # Convertendo todos os elementos para string e maiúsculas

    inicio = 0
    fim = len(vetor) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2  # Calcula o ponto médio

        if vetor[meio] == valor:
            return meio  # Valor encontrado, retorna o índice
        elif vetor[meio] < valor:
            inicio = meio + 1  # Procura na metade superior
        else:
            fim = meio - 1  # Procura na metade inferior

    return -1  # Valor não encontrado

# Exemplo de uso
vetor = ['A', 'b', '1', 'c', '3', 'Z']
valor_procurado = 'z'
indice = pesquisa_binaria(sorted(vetor), valor_procurado)  # O vetor precisa estar ordenado
print(f"Índice encontrado: {indice}")
