def main():
    massa_inicial = float(input("Digite a massa inicial em gramas: "))
    
    # Definir a massa alvo
    massa_alvo = 0.5
    tempo = 0 

    while massa_inicial >= massa_alvo:
        massa_inicial /= 2  # A massa perde metade
        tempo += 50  # Incrementa 50 segundos

    print(f"Tempo necessário para que a massa seja menor que 0,5g: {tempo} segundos")

if __name__ == "__main__":
    main()
