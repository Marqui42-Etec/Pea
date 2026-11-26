matriz_A = []
matriz_B = []
matriz_C = []


for i in range(15):
    n = int(input(f"Digite um número para a ({i}) da Matriz_A: "))
    matriz_A.append(n)
print()
for i in range(15):
    n = int(input(f"Digite um número para a ({i}) da Matriz_B: "))
    matriz_B.append(n)
print()

for i in range(15):
    linha = []
    for j in range(2):
        if j == 0:
            item = matriz_A[i]
        if j == 1:
            item = matriz_B[i]
        linha.append(item)
    matriz_C.append(linha)

print(f"\nMatriz A: \n   {matriz_A}")
print(f"\nMatriz B: \n   {matriz_B}")
print(f"\nMatriz C: \n")
for linha in matriz_C:
    print(linha)
    