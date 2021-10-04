nota = int(input("Digite uma nota de 0 a 10: "))
while nota < 0 or nota > 10:
    print("Nota informada não é válida!!")
    nota = int(input("Digite novamente uma nota de 0 a 10: "))

print(f"A nota informada foi: {nota}")
