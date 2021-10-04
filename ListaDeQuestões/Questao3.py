name = input("Informe seu nome: ")
while len(name) <= 3:
    print("Nome informado tem que ser maior que 3 caracteres!")
    name = input("Informe seu nome novamente: ")

age = int(input("Informe sua idade: "))
while age < 0 or age > 150:
    print("Idade informado está fora dos limnites!")
    age = int(input("Informe sua idade novamente: "))

salary = float(input("Informe seu salário: "))
while salary < 0:
    print("Salário menor que zero!")
    salary = float(input("Informe seu salário novamente: "))

gender = input("Informe seu sexo - 'f' ou 'm': ").upper()
checkGenderStatus = True
while checkGenderStatus:
    if (gender == 'F' or gender == 'M'):
        checkGenderStatus = False
    else:
        print("Sexo inválido!")
        gender = input("Informe seu sexo novamente - 'f' ou 'm': ").upper()
        checkGenderStatus = True


def verifyMaritalStatus(answer):
    listaMaritalStatus = ['S', 'C', 'V', 'D']
    statusVericationMaritalStatus = False
    for statusMaritalStatus in listaMaritalStatus:
        if (answer == statusMaritalStatus):
            statusVericationMaritalStatus = True

    return statusVericationMaritalStatus


maritalStatus = input(
    "Informe seu estado civil - 's', 'c', 'v', 'd': ").upper()
checkMaritalStatus = True
while checkMaritalStatus:
    if verifyMaritalStatus(maritalStatus):
        checkMaritalStatus = False
    else:
        print("Estado Civil Inválido!")
        maritalStatus = input(
            "Informe seu estado civil novamente - 's', 'c', 'v', 'd': ").upper()
