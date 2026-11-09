################################################################
# Descrição: lê dois números e imprime o maior deles           #
# Parâmetros de entrada: dois números digitados pelo usuário   #
# Valores de saída: o maior número entre os dois               #
# Autor: Matheus Alves de Souza Marqui                         #
################################################################

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

if n1 > n2:
    print("O maior é", n1)
elif n2 > n1:
    print("O maior é", n2)
else:
    print("Os números são iguais")