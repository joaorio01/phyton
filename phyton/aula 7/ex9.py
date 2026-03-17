
def datamagic (dia, mes, ano):
    if ano == dia * mes:
        return True
    else:
        return False
    
dia = int(input("digite o dia: ") )
mes =  int(input("digite o mês: "))
ano = int(input("Digite o ano: "))

if datamagic(dia, mes, ano):
    print("Sua data é magica")
else:
    print("Sua data não é magica, seu bosta")
    
