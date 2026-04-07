#Faça um programa que: Peça 10 números reais do usuário.
#Armazene-os em uma lista e diga qual o índice do maior e seu
#valor
numeros = []
for i in range(10):
    valores = int(input(f"Digite o {i+1}º número: "))
    numeros.append(valores)

maior_valor = max(numeros)
indice = numeros.index(maior_valor)

print("Lista:", numeros)
print("Maior valor:", maior_valor)
print("Índice do maior valor:", indice)
