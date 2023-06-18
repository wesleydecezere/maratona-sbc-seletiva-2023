entrada = list(map(int, input().split()))
entrada.sort()

erro = list(map(lambda x: 94 - int(x), entrada))

print(entrada)
print(erro)