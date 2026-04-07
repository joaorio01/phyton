lista = []

for i in range (10):
    num = int(input("Digite um número: "))
    lista.append(num)

for i in range (2, 10):
    if lista[i] > lista[i-1] + lista[i-2]:
        print(lista[i])