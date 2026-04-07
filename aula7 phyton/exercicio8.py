lista = []

while True:
     palavra =  input("Digite uma palavra (Escreva nada para parar): ")
     if palavra == "":
         break
     
     lista.append(palavra)

for palavra in lista:
     print(palavra)
     