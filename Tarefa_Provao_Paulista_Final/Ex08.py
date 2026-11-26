################################################################
# Descrição: soma os cem primeiros números naturais            #
# Parâmetros de entrada: não há                                #
# Valores de saída: o resultado de 1+2+3+...+100               #
# Autor: Matheus Alves de Souza Marqui                         #
################################################################

soma = 0

for i in range(1, 101):
    soma = soma + i

print("A soma dos cem primeiros números naturais é:", soma)