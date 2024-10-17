# Função para cadastrar funcionários com tratamento de erros
def cadastrar_funcionarios():
    funcionarios = []  # Lista para armazenar os dados dos funcionários

    # Obtém o número de funcionários com tratamento de erro
    while True:
        try:
            n = int(input("Quantos funcionários deseja cadastrar? "))
            if n > 0:
                break
            else:
                print("O número deve ser maior que 0.")
        except ValueError:
            print("Entrada inválida! Digite um número inteiro.")

    # Cadastro dos funcionários
    for _ in range(n):
        # Obtém o nome com validação
        nome = input("Digite o nome do funcionário: ").strip()
        while not nome:  # Verifica se o nome não está vazio
            nome = input("Nome inválido! Digite novamente: ").strip()

        # Obtém o salário com validação
        while True:
            try:
                salario = float(input(f"Digite o salário de {nome}: "))
                if salario > 0:
                    break
                else:
                    print("O salário deve ser maior que 0.")
            except ValueError:
                print("Entrada inválida! Digite um número para o salário.")

        # Adiciona o funcionário à lista
        funcionarios.append({'nome': nome, 'salario': salario})

    return funcionarios

# Função para ordenar funcionários por salário (crescente)
def ordenar_por_salario_crescente(funcionarios):
    funcionarios_ordenados = sorted(funcionarios, key=lambda f: f['salario'])
    print("\nFuncionários em ordem crescente de salário:")
    for f in funcionarios_ordenados:
        print(f"Nome: {f['nome']}, Salário: R${f['salario']:.2f}")

# Função para ordenar funcionários por salário (decrescente)
def ordenar_por_salario_decrescente(funcionarios):
    funcionarios_ordenados = sorted(funcionarios, key=lambda f: f['salario'], reverse=True)
    print("\nFuncionários em ordem decrescente de salário:")
    for f in funcionarios_ordenados:
        print(f"Nome: {f['nome']}, Salário: R${f['salario']:.2f}")

# Função para ordenar funcionários por nome (ordem alfabética)
def ordenar_por_nome(funcionarios):
    funcionarios_ordenados = sorted(funcionarios, key=lambda f: f['nome'].lower())  # Para ignorar maiúsculas/minúsculas
    print("\nFuncionários em ordem alfabética:")
    for f in funcionarios_ordenados:
        print(f"Nome: {f['nome']}, Salário: R${f['salario']:.2f}")

# Exemplo de uso
funcionarios = cadastrar_funcionarios()  # Cadastra os funcionários

# Listar em diferentes ordens
ordenar_por_salario_crescente(funcionarios)  # Ordem crescente de salário
ordenar_por_salario_decrescente(funcionarios)  # Ordem decrescente de salário
ordenar_por_nome(funcionarios)  # Ordem alfabética
