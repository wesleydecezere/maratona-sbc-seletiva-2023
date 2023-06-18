n = int(input())
palpites = list(map(int, input().split()))
erros = list(map(int, input().split()))

valores = {}
x1 = map(lambda palpite, erro: palpite - erro, palpites, erros)
x2 = map(lambda palpite, erro: palpite + erro, palpites, erros)

valores = list(x1) + list(x2)
valores_unicos = set(valores)
print(valores)
print(valores_unicos)

valores_possiveis = [x for x in valores if x not in valores_unicos]

print(valores_possiveis)
