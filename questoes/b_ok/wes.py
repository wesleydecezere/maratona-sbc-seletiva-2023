valores = map(int, input().split())
objetivo = input()


fatores = {
    ('A', 'B'): 2/3,
    ('B', 'A'): 3/2,

    ('A', 'C'): 2/5,
    ('C', 'A'): 5/2,

    ('B', 'C'): 3/5,
    ('C', 'B'): 5/3
}

total = 0
for i, valor in enumerate(valores):
    num = objetivo

    if i == 0:
        den = 'A'
    if i == 1:
        den = 'B'
    if i == 2:
        den = 'C'

    if den == num:
        total += valor
    else:
        total += (valor * fatores[(den, num)])

print(int(total))