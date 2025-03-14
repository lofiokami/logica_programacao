qn = int(input("Digite a quantidade de notas :"))
sn = 0


for i in range(1, qn +1):
    nota = float(input(f"Digite sua nota {i} :"))
    sn = sn + nota 


media = sn / qn 
print(f"A soma das medias é {media:.2f}")


if media >= 6:
    print("Aluno aprovado.")
else:
    print("Aluno reprovado.")