firstNumberInteger = int(input("Digite um número inteiro: "))
secondNumberInteger = int(input("Digite outro número inteiro: "))
numberReal = float(input("Digite um número real: "))

calc1 = (2 * firstNumberInteger) * (secondNumberInteger / 2)
calc2 = (3 * firstNumberInteger) + numberReal
calc3 = numberReal ** 3

print(
    f"O resultado do produto do dobro do primeiro com metade do segundo: {calc1} ")
print(f"O resultado da soma do triplo do primeiro com o terceiro: {calc2} ")
print(f"O resultado do terceiro elevado ao cubo: {calc3} ")
