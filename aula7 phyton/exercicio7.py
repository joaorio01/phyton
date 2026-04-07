temperaturas=[-10,-8, 0, 1, 2, 5,-2,-4]

menor = min(temperaturas)
maior = max(temperaturas)

soma = 0
for t in temperaturas:
    soma += t

media = soma / len(temperaturas)

print("Temperaturas:", temperaturas)
print("Menor temperatura:", menor)
print("Maior temperatura:", maior)
print("Média das temperaturas:", media)