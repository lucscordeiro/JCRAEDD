def main():
    total_mercadorias = 0
    faturamento_total = 0
    lucro_total = 0

    while True:
        
        try:
            preco_custo = float(input("Digite o preço de custo da mercadoria (ou -1 para encerrar): "))
            if preco_custo == -1:
                break

            preco_venda = float(input("Digite o preço de venda da mercadoria: "))
            quantidade_vendida = int(input("Digite a quantidade vendida da mercadoria: "))
            
            faturamento = preco_venda * quantidade_vendida
            lucro = (preco_venda - preco_custo) * quantidade_vendida
            
            faturamento_total += faturamento
            lucro_total += lucro
            total_mercadorias += 1
        
        except ValueError:
            print("Entrada inválida! Por favor, insira valores numéricos.")

    
    print(f"\nNúmero total de mercadorias diferentes: {total_mercadorias}")
    print(f"Faturamento total: R$ {faturamento_total:.2f}")
    print(f"Lucro total: R$ {lucro_total:.2f}")

if __name__ == "__main__":
    main()
