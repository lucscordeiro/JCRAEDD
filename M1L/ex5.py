# Em Python, os inteiros podem crescer dinamicamente, então não há risco de overflow como em outras linguagens (por exemplo, C ou Java).

def main():
    total_quadrados = 64
    total_graos = 0
    
    for i in range(total_quadrados):
        # O número de grãos no quadrado i é 2^i
        graos_no_quadrado = 2 ** i
        
        total_graos += graos_no_quadrado
        
        print(f"Quadrado {i + 1}: {graos_no_quadrado} grãos")
    
    print(f"\nTotal de grãos de milho no tabuleiro: {total_graos}")

if __name__ == "__main__":
    main()
