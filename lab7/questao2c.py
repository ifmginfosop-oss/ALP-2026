# O erro era começar com infinito positivo
# Agora começa com um número muito pequeno
maior = float('-inf')

contador = 1

while contador <= 10:
    num = int(input("Digite um número: "))

    # Verifica se o número digitado é maior
    if num > maior:
        maior = num

    contador += 1

print("O maior número é:", maior)
