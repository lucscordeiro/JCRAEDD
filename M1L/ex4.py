def main():
    cont = 0
    soma = 0
    
    while True:
        try:
            idade = int(input("Digite a idade do aluno (ou 0 para encerrar): "))

            if idade == 0:
                break

            if idade < 0:
                print("Idade negativa não é válida. Por favor, redigite.")
                continue
            
            soma += idade
            cont += 1

            # print(cont/soma)

        except ValueError:
            print("Entrada inválida! Por favor, digite um número válido.")
    
    if cont > 0:
        media = soma / cont
        print(f"A média aritmética das idades é: {media:.2f}")
    else:
        print("Nenhuma idade válida foi registrada.")

if __name__ == "__main__":
    main()