"""
1. Implemente um programa estruturado e recursivo para pesquisa linear.
Faça uma função de busca chamada pesquisaLR que receba como parâmetro o valor a ser 
encontrado e a referência do vetor onde a busca será efetuada. A função retornará -1, 
caso não encontre o item, ou retornará o índice, caso o encontre.
"""


def pesquisaLR(vetor, valor, indice=0):
    # Verifica se o índice atingiu o final do vetor
    # Caso tenha percorrido todo o vetor e não encontrou o valor, retorna -1
    if indice == len(vetor):
        return -1  # Valor não encontrado

    # Verifica se o valor na posição atual do vetor é o que estamos procurando
    if vetor[indice] == valor:
        return indice  # Retorna o índice onde o valor foi encontrado

    # Caso o valor não tenha sido encontrado, chamamos a função novamente
    # Aumentando o índice para verificar o próximo elemento
    return pesquisaLR(vetor, valor, indice + 1)

# Exemplo de uso
vetor = [5, 'a', 3, 'b', 9]
valor_procurado = 'b'

indice = pesquisaLR(vetor, valor_procurado)

if indice != -1:
    print(f"Índice encontrado: {indice}")
else:
    print("Valor não encontrado no vetor.")

