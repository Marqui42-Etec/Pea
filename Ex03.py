################################################################
# Descrição: verifica se a letra digitada é F ou M             #
# Parâmetros de entrada: uma letra (F ou M)                    #
# Valores de saída: F - Feminino, M - Masculino ou             #
#                   Sexo Inválido                              #
# Autor: Matheus Alves de Souza Marqui                         #
################################################################

letra = input("Digite uma letra (F ou M): ")

if letra == "F":
    print("F - Feminino")
elif letra == "M":
    print("M - Masculino")
else:
    print("Sexo Inválido")