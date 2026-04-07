
quantidade = int(input("Digite a quantidade de números da sua lista: "))

valores = []

for i in range(quantidade):
    num = int(input("Digite a os numeros: "))
    valores.append(num)

valores.reverse()

print("Ordem inversa:")
for num in valores:
    print(num)
