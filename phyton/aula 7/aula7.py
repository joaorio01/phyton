quantidade = int(input("Quantos números serão digitados? "))
cont_primos = 0

for i in range(quantidade):
    num = int(input("Digite um número natural: "))
    divisores = 0

    for i in range(1, num + 1):
        if num % i == 0:
            divisores += 1

    if divisores == 2:
        cont_primos += 1

print("Quantidade de números primos:", cont_primos)