def main():

    boi_mais_gordo = None
    boi_mais_magro = None
    peso_total = 0

    while True:
        try:
            
            numero_boi = int(input("Digite o número de identificação do boi (ou um número negativo para encerrar): "))
            
            # Verifica se o número de identificação é negativo para parar o programa
            if numero_boi < 0:
                break
            
            peso_boi = float(input(f"Digite o peso do boi de identificação {numero_boi}: "))
            
            peso_total += peso_boi
            
            # Se for o primeiro boi, ele será o mais gordo e o mais magro
            if boi_mais_gordo is None or boi_mais_magro is None:
                boi_mais_gordo = (numero_boi, peso_boi)
                boi_mais_magro = (numero_boi, peso_boi)
            else:
                # Atualizar o boi mais gordo, se o peso for maior que o do boi mais gordo atual
                if peso_boi > boi_mais_gordo[1]:
                    boi_mais_gordo = (numero_boi, peso_boi)
                
                # Atualizar o boi mais magro, se o peso for menor que o do boi mais magro atual
                if peso_boi < boi_mais_magro[1]:
                    boi_mais_magro = (numero_boi, peso_boi)
        
        except ValueError:

            print("Entrada inválida! Por favor, digite um número válido.")
    
    if boi_mais_gordo and boi_mais_magro:
        print("\nResultados:")
        print(f"Boi mais gordo: ID {boi_mais_gordo[0]}, Peso: {boi_mais_gordo[1]:.2f} kg")
        print(f"Boi mais magro: ID {boi_mais_magro[0]}, Peso: {boi_mais_magro[1]:.2f} kg")
        print(f"Peso total dos bois: {peso_total:.2f} kg")
    else:
        print("\nNenhum boi foi registrado.")

if __name__ == "__main__":
    main()