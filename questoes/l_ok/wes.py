n, m = map(int, input().split())
s = int(input())

def calc(x, y, r):
    xi = x-r
    xf = x+r
    yi = y-r
    yf = y+r

    xi = xi if (xi > 0) else 1
    xf = xf if (xf < m) else m
    yi = yi if (yi > 0) else 1
    yf = yf if (yf < n) else n

    return (xi, xf, yi, yf)

casas = 0
for _ in range(s):
    y, x, r = map(int, input().split())
    xi, xf, yi, yf = calc(x, y, r)

    casas += (xf-xi+1) * (yf-yi+1)

casas /= n*m

print(int(casas))




