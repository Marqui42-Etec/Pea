################################################################
# Descrição: mostra os números ímpares de 0 a 20               #
# Parâmetros de entrada: não há                                #
# Valores de saída: os ímpares existentes entre 0 e 20         #
# Autor: Matheus Alves de Souza Marqui                         #
################################################################

for i in range(0, 21):
    if i % 2 != 0:
        print(i)