################################################################
# Descrição: mostra a saudação conforme o turno de estudo      #
# Parâmetros de entrada: uma letra (M, V ou N)                 #
# Valores de saída: Bom Dia!, Boa Tarde!, Boa Noite! ou        #
#                   Valor Inválido!                            #
# Autor: Matheus Alves de Souza Marqui                         #
################################################################

turno = input("Digite o turno (M - Matutino, V - Vespertino ou N - Noturno): ")

if turno == "M":
    print("Bom Dia!")
elif turno == "V":
    print("Boa Tarde!")
elif turno == "N":
    print("Boa Noite!")
else:
    print("Valor Inválido!")