numero = int(input("Digite até onde a taboada deve ir :"))


for x in range (1, numero+1):
    print("-------------------------------")
    for i in range (1,11):
        resultado = i * numero 
        print(f"{x} * {i} = {resultado}")