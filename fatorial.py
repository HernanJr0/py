num = int(input("Digite um número: "))

resultado = 1

for i in range(2, num + 1):
    resultado *= i

print(f"O fatorial de {num} é {resultado}")