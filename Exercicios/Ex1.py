matriz_A = []
matriz_B = []
for j in range(15):
    n = int(input(f"Digite um número para a posição ({j}): "))
    matriz_A.append(n)

for item in matriz_A:
    x = 1
    for i in range(1, item + 1):
        x = x * i
    matriz_B.append(x)

matriz_B.sort()

print(f"\nMatriz A = \n   {matriz_A}")
print(f"\nMatriz B em ordem crescente = \n   {matriz_B}")
