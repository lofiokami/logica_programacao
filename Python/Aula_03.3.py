print("Calculadora - Exemplo de Operações: ")
print("+  Adição - Subtração * Multiplicação / Divisão ")


n1 = float(input("Digite o primeiro numero :"))
operacao = input("Digite a operação :")
n2 = float(input("Digite o segundo numero :"))
resultado = 0


if operacao == "+":
    resultado = n1 + n2
elif operacao == "-":
    resultado = n1 - n2
elif operacao == "*":
    resultado = n1 * n2
elif operacao == "/":
    resultado = n1 / n2
else:
    print("Operação invalida.")


print("O resultado é: ", str(resultado))