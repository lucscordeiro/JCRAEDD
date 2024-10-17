"""
6. Dada uma tabela de horários de ônibus que fazem viagens para as diversas cidades 
do Estado, escreva um programa que possibilite a localização dos horários de saída e 
de chegada quando se forneça o destino.
"""

tabela_horarios = [
    {'destino': 'CidadeA', 'saida': '08:00', 'chegada': '10:00'},
    {'destino': 'CidadeB', 'saida': '09:30', 'chegada': '11:45'},
    {'destino': 'CidadeC', 'saida': '11:00', 'chegada': '13:30'},
    {'destino': 'Jacarei', 'saida': '12:00', 'chegada': '14:30'},
]

def localizar_horarios(destino):
    # Normaliza os dados fornecidos
    destino = destino.lower()  
    
    # Percorre a lista de horários para encontrar o destino
    for horario in tabela_horarios:
        # Compara o destino em letras minúsculas
        if horario['destino'].lower() == destino:
            # Se o destino for encontrado, exibe os horários
            print(f"Horários para {horario['destino']}:")
            print(f"Saída: {horario['saida']}")
            print(f"Chegada: {horario['chegada']}")
            return  # Sai da função após encontrar e exibir o horário
    
    # Se o destino não for encontrado, informa o usuário
    print(f"Destino {destino} não encontrado.")

# Exemplo de uso
destino_usuario = input("Informe o destino: ")  # Permite que o usuário insira o destino
localizar_horarios(destino_usuario)  # Chama a função para mostrar os horários para o destino fornecido

