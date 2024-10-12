"""
1. Implemente um programa estruturado e recursivo para pesquisa linear.
Faça uma função de busca chamada pesquisaLR que receba como parâmetro o valor a ser 
encontrado e a referência do vetor onde a busca será efetuada. A função retornará -1, 
caso não encontre o item, ou retornará o índice, caso o encontre.
"""


def pesquisaLR(vetor, valor, indice=0):
    # Verifica se o índice está além do tamanho do vetor
    if indice == len(vetor):
        return -1  # Retorna -1 caso não encontre o valor

    # Verifica se o valor na posição atual é o que procuramos
    if vetor[indice] == valor:
        return indice  # Retorna o índice onde o valor foi encontrado

    # Chamada recursiva para o próximo elemento
    return pesquisaLR(vetor, valor, indice + 1)

# Exemplo de uso
vetor = [5, 'a', 3, 'b', 9]
valor_procurado = 'b'
indice = pesquisaLR(vetor, valor_procurado)
print(f"Índice encontrado: {indice}")
