name = input("Informe seu nome: ")
password = input("Informe sua senha: ")
while (name == password):
    print("Nome e senha não podem ser iguais!")
    print("Informe as informações novamente")
    name = input("Informe seu nome: ")
    password = input("Informe sua senha: ")
print(f"Acesso autorizado, {name}")
