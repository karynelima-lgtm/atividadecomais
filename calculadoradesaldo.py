gastos = []
entradas = []

print("insira os gastos, ao finalizar os gastos digite 'sair'")
negativo = input("Gasto: ")
while negativo != "sair":
    gastos.append(float(negativo))
    negativo = input("Gasto: ")

print("Insira as entradas, ao finalizar as entradas3 digite 'sair'")
positivo = input("Entrada: ")
while positivo != "sair":
    entradas.append(float(positivo))
    positivo = input("Entrada: ")

gastostotal = sum(gastos)
print("O total de gastos: ", gastostotal)
print("O total de entradas é: ", sum(entradas))
saldototal = sum(entradas) - sum(gastos)
print("O saldo total é: ", saldototal)