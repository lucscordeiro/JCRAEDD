"""
6. Dada uma tabela de horários de ônibus que fazem viagens para as diversas cidades 
do Estado, escreva um programa que possibilite a localização dos horários de saída e 
de chegada quando se forneça o destino.
"""


# Dados fictícios da tabela de horários
tabela_horarios = {
    'CidadeA': {'saida': '08:00', 'chegada': '10:00'},
    'CidadeB': {'saida': '09:30', 'chegada': '11:45'},
    'CidadeC': {'saida': '11:00', 'chegada': '13:30'},
}

def localizar_horarios(destino):
    destino = destino.capitalize()  # Normaliza a entrada
    if destino in tabela_horarios:
        horarios = tabela_horarios[destino]
        print(f"Horários para {destino}:")
        print(f"Saída: {horarios['saida']}")
        print(f"Chegada: {horarios['chegada']}")
    else:
        print(f"Destino {destino} não encontrado.")

# Exemplo de uso
localizar_horarios('cidadeb')
