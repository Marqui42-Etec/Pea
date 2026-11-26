################################################################
# Descrição: soma os valores pares de 1 até 500                #
# Parâmetros de entrada: não há                                #
# Valores de saída: o somatório dos pares de 1 a 500           #
# Autor: Matheus Alves de Souza Marqui                         #
################################################################

soma = 0

for i in range(1, 501):
    if i % 2 == 0:
        soma = soma + i

print("O somatório dos pares de 1 a 500 é:", soma)