from math import sqrt

n, k = map(int, input().split())
div = n * 2 + 1

pos_k = int(sqrt(k))
max_pos = 2 * n
alice = (max_pos - pos_k + 1) * (max_pos - pos_k + 1)
# print(int(alice))

for i in range(2 * n, 0, -1):
  if i == pos_k:
    continue
  val = i**2
  if abs(val - k) % div == 0:
    print(val)
    break