def pode_doar(sexo, peso):
    if sexo == 'F' and peso >= 50:
        return True
    elif sexo == 'M' and peso >= 60:
        return True
    else:
        return False

sexo = input("Digite o sexo (M/F): ")
peso = float(input("Digite o peso: "))

if pode_doar(sexo, peso):
    print("Apta(o) a doar sangue")
else:
    print("Não apta(o) a doar sangue")

