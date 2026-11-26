matriz_A = []
matriz_B = []
matriz_C = []

for j in range(10):
    n = int(input(f"Digite um número para a ({j}) da Matriz_A: "))
    matriz_A.append(n)

for j in range(10):
    n = int(input(f"Digite um número para a ({j}) da Matriz_B: "))
    matriz_B.append(n)

for i in range(10):
    item = matriz_A[i] ** 2 + matriz_B[i] ** 2
    matriz_C.append(item)

print(f"\nMatriz A: \n   {matriz_A}")
print(f"\nMatriz B: \n   {matriz_B}")
print(f"\nMatriz C: \n   {matriz_C}")
