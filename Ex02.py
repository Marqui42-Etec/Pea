################################################################
# Descrição: verifica se um valor é positivo ou negativo       #
# Parâmetros de entrada: um número digitado pelo usuário       #
# Valores de saída: mensagem dizendo se o valor é              #
#                   positivo, negativo ou zero                 #
# Autor: Matheus Alves de Souza Marqui                         #
################################################################

num = float(input("Digite um valor: "))

if num > 0:
    print("O valor é positivo")
elif num < 0:
    print("O valor é negativo")
else:
    print("O valor é zero")