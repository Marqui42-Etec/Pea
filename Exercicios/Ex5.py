matriz = []

for i in range(4):
    linha = []
    for j in range(5):
        n = int(input(f"Digite um número para a posição ({i}, {j}) da Matriz: "))
        linha.append(n)
    matriz.append(linha)

print()
for linha in matriz:
    print(linha)
