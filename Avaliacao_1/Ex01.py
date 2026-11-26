################################################################
# Descrição: Potenciação com base 3, expoente de 0 a 15        #
# Parâmetros de entrada: nenhum, basta iniciar o programa      #
#                                                              #
# Valores de saída: valores com 3, 9, 27...                    #
#                                                              #
# Autor: Matheus Alves de Souza Marqui                         #
################################################################
comeco = 1
print(comeco)
num = comeco
for i in range(1, 16):
    num *= 3
    print(num)
