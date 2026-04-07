valores = []

for i in range (10):
    num = int(input(f"Digite o {i+1} número: "))
    valores.append(num)

soma_pares = 0
soma_indice = 0

for i in range (10):
    if valores [i] % 2 == 0:
        soma_pares += valores[i]

if i % 2 == 0:
    soma_indice += valores[i]

print("Lista:", valores)
print("Soma dos valores pares:", soma_pares)
print("Soma dos índices pares:", soma_indices_pares)