################################################################
# Descrição: calcula a média de duas notas e mostra a          #
#            situação do aluno                                 #
# Parâmetros de entrada: duas notas parciais                   #
# Valores de saída: Aprovado, Reprovado ou Aprovado com        #
#                   Distinção                                  #
# Autor: Matheus Alves de Souza Marqui                         #
################################################################

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

if media == 10:
    print("Aprovado com Distinção")
elif media >= 7:
    print("Aprovado")
else:
    print("Reprovado")