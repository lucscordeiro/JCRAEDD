def main():

    maior = None
    menor = None
    soma = 0
    cont = 0

    while True:
        try:
            numero = float(input("Digite um número positivo (negativo para encerrar): "))

            if numero < 0:
                break

            if (maior is None) or (numero > maior):
                maior = numero
            
            if(menor is None) or (numero < menor):
                menor = numero

            soma += numero
            cont += 1
        except ValueError:
            print("Entrada inválida! Por favor, digite um número válido.")

    if cont > 0:
        media = soma / cont
        print("\nResultados:")
        print(f"Maior número: {maior}")
        print(f"Menor número: {menor}")
        print(f"Média dos números: {media:.2f}")
    else:
        print("\nNenhum número positivo foi digitado.")


if __name__ == "__main__":
    main()