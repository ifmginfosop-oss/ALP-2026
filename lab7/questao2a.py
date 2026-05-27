
N = int(input("Quantos números quer digitar? "))

contador = 1
impares = 0

while contador <= N:
    num = int(input("Digite um número: "))

    # Verifica se o número é ímpar
    if num % 2 != 0:
        impares += 1

    # ERRO: o contador não aumentava
    # Correção: incrementar o contador
    contador += 1

print(f"Quantidade de ímpares: {impares}")
