import time

n = int(input())
palpites = list(map(int, input().split()))
erros = list(map(int, input().split()))

palpites.sort()
erros.sort(reverse=True)

print(palpites)
print(erros)

def soma():
    p = sum(palpites)
    e = sum(erros)

    a = (p + e) / n
    b = (p - e) / n

    return int(a), int(b)

def troca():
    first = erros.pop(0)
    erros.append(-first)
    erros.sort(reverse=True)

a, b = soma()
print(a, b)

while erros[0] + palpites[0] != a:
    troca()
    print(palpites)
    print(erros)

    a, b = soma()
    print(a, b)
    time.sleep(1)


