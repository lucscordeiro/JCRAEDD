"""
3. Um vetor de tamanho n, pode conter elementos do alfabeto e numerais 0 a 9. 
Escreva um algoritmo que seja capaz de localizar, pelo método binário, um caractere 
fornecido pelo usuário. Se esse caractere for uma letra, o usuário poderá fornecê-la 
para a busca no formato maiúsculo ou minúsculo.
"""

def buscaBinaria(vetor, valor, inicio, fim):
    # Caso base: Se o início ultrapassar o fim, significa que o valor não está no vetor
    if inicio > fim:
        return -1  # Valor não encontrado
    
    # Calcula o índice do meio do vetor
    meio = (inicio + fim) // 2
    
    # Compara o valor no meio com o valor procurado
    if vetor[meio] == valor:
        return meio  # Retorna o índice se o valor foi encontrado
    
    # Se o valor procurado for menor que o valor no meio, pesquisa na metade esquerda
    elif valor < vetor[meio]:
        return buscaBinaria(vetor, valor, inicio, meio - 1)
    
    # Caso contrário, pesquisa na metade direita
    else:
        return buscaBinaria(vetor, valor, meio + 1, fim)

# Função principal para lidar com a entrada do usuário e garantir a uniformidade do vetor
def pesquisaBinaria(vetor, valor_procurado):
    # Converte todos os elementos do vetor e o valor procurado para minúsculas para uniformizar
    vetor = [str(x).lower() for x in vetor]
    valor_procurado = str(valor_procurado).lower()

    # Ordena o vetor, já que a busca binária só funciona em vetores ordenados
    vetor.sort()

    # Chama a função de busca binária passando o vetor ordenado
    return buscaBinaria(vetor, valor_procurado, 0, len(vetor) - 1)

# Exemplo de uso:
vetor = ['A', 'z', '5', 'B', '7', 'e', '1', '3', 'C']
valor_procurado = 'b'

indice = pesquisaBinaria(vetor, valor_procurado)

if indice != -1:
    print(f"Valor '{valor_procurado}' encontrado no índice {indice}.")
else:
    print(f"Valor '{valor_procurado}' não encontrado.")
