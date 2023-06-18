n = 10
div = n * 2 + 1
valores = [(x + 1) * (x + 1) for x in range(2 * n)]
lis = []

for idx, valor_1 in enumerate(valores):
  for valor_2 in valores:
    if valor_1 == valor_2:
      continue
    if abs(valor_1 - valor_2) % div == 0:
      lis.append("{} -> {} ".format(valor_1, valor_2))
      print(valor_1, "->", valor_2)
print(len(lis) == len(valores))
