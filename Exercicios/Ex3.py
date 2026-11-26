matriz_A = []
matriz_B = []
matriz_C = []
matriz_D = []

for i in range(15):
    n = int(input(f"Digite um número para a ({i}) da Matriz_A: "))
    matriz_A.append(n)
print()
for i in range(15):
    n = int(input(f"Digite um número para a ({i}) da Matriz_B: "))
    matriz_B.append(n)
print()
for i in range(15):
    n = int(input(f"Digite um número para a ({i}) da Matriz_C: "))
    matriz_C.append(n)

for i in range(15):
    x = (matriz_A[i] + matriz_B[i] + matriz_C[i]) ** 3
    matriz_D.append(x)

print(f"\nMatriz A: \n   {matriz_A}")
print(f"\nMatriz B: \n   {matriz_B}")
print(f"\nMatriz C: \n   {matriz_C}")
print(f"\nMatriz D: \n   {matriz_D}")
