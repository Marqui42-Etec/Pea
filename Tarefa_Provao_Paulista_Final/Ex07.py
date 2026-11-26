################################################################
# Descrição: mostra a tabuada de um número qualquer            #
# Parâmetros de entrada: um número inteiro                     #
# Valores de saída: a tabuada do número na forma tradicional   #
# Autor: Matheus Alves de Souza Marqui                         #
################################################################

num = int(input("Digite um número para ver a tabuada: "))

for i in range(1, 11):
    print(num, "x", i, "=", num * i)