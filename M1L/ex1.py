def menu():
    print("=== Conversor de Moedas ===")
    print("1 - Dólar Americano (USD)")
    print("2 - Euro (EUR)")
    print("3 - Libra Esterlina (GBP)")
    print("4 - Yuan Chinês (CNY)")

def obter_fator_conversao(escolha):
    fatores = {
        1: 3.258,
        2: 4.095,
        3: 4.529,
        4: 0.515
    }
    return fatores.get(escolha, None)

def converter_reais_para_moeda(valor_reais, fator):
    return valor_reais / fator

def main():

    menu()

    try:
        escolha = int(input("Escolha a moeda para conversão (1-4): "))

        if escolha not in [1, 2, 3, 4]:
            print("Escolha inválida. Por favor, selecione uma opção de 1 a 4.")
            return

        valor_reais = float(input("Digite o valor em R$: "))

        fator = obter_fator_conversao(escolha)

        valor_convertido = converter_reais_para_moeda(valor_reais, fator)

        moedas = {
            1: "Dólar Americano (USD)",
            2: "Euro (EUR)",
            3: "Libra Esterlina (GBP)",
            4: "Yuan Chinês (CNY)"
        }

        nome_moeda = moedas.get(escolha)

        print(f"\n{valor_reais:.2f} R$ equivalem a {valor_convertido:.2f} {nome_moeda}.")

    except ValueError:
         print("Entrada inválida. Por favor, insira números válidos.")

if __name__ == "__main__":
    main()