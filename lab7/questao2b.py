soma = 0
contador = 1

# O erro era usar a soma como condição
# Agora o programa repete 10 vezes
while contador <= 10:
    num = int(input("Digite um número para somar: "))

    soma += num

    contador += 1

print("Resultado da soma:", soma)
