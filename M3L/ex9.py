"""
9. Faça um programa que cadastre o nome e o salário de n funcionários. Usando um 
método de ordenação diferente para cada item a seguir, liste todos os dados dos 
funcionários das seguintes formas: 
a. Em ordem crescente de salário; 
b. Em ordem decrescente de salário; 
c. Em ordem alfabética.
"""


def cadastrar_funcionarios():
    funcionarios = []
    n = int(input("Quantos funcionários deseja cadastrar? "))

    for _ in range(n):
        nome = input("Nome: ")
        salario = float(input("Salário: "))
        funcionarios.append({'nome': nome, 'salario': salario})

    return funcionarios

def ordenar_salario_crescente(funcionarios):
    return sorted(funcionarios, key=lambda x: x['salario'])

def ordenar_salario_decrescente(funcionarios):
    return sorted(funcionarios, key=lambda x: x['salario'], reverse=True)

def ordenar_nome_alfabetico(funcionarios):
    return sorted(funcionarios, key=lambda x: x['nome'].lower())

# Exemplo de uso
funcionarios = cadastrar_funcionarios()
print("Crescente por salário:")
print(ordenar_salario_crescente(funcionarios))

print("Decrescente por salário:")
print(ordenar_salario_decrescente(funcionarios))

print("Ordem alfabética:")
print(ordenar_nome_alfabetico(funcionarios))
