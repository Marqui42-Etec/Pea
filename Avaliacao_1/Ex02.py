################################################################
# Descrição: Somatório potenciação de base, expoente de 0 a 63 #
# Parâmetros de entrada: nenhum, basta iniciar o programa      #
#                                                              #
# Valores de saída: valores com 1, 2, 4, 8...                  #
#                                                              #
# Autor: Matheus Alves de Souza Marqui                         #
################################################################
numero = 1
soma = 1
for i in range(2, 64):
    numero *= 2
    soma += numero

print(f"A soma é : {soma}")