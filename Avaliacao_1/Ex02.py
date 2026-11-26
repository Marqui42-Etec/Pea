################################################################
# Descrição: Somatório potenciação de base, expoente de 0 a 63 #
# Parâmetros de entrada: nenhum, basta iniciar o programa      #
#                                                              #
# Valores de saída: valores com 1, 2, 4, 8...                  #
#                                                              #
# Autor: Matheus Alves de Souza Marqui                         #
################################################################
soma = 0
for i in range(0, 64):
    soma += 2 ** i

print(f"A soma é : {soma}")