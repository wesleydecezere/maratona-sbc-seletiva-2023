from collections import deque

def press_keys(lights):
    queue = deque([(lights, '', 0)])  # Fila de estados (luzes, sequência, movimentos)
    visited = set([lights])  # Conjunto de estados visitados

    while queue:
        current_lights, sequence, moves = queue.popleft()

        if all(current_lights):  # Se todas as luzes estão acesas
            return moves, sequence

        if moves > 10:  # Se excedeu o número máximo de movimentos
            break

        for i in range(1, 11):
            next_lights = current_lights[:]
            press_key(next_lights, i)  # Pressiona a tecla i

            if next_lights not in visited:
                queue.append((next_lights, sequence + str(i) + ' ', moves + 1))
                visited.add(next_lights)

    return -1


def press_key(lights, key):
    hexagons = {
        1: [1, 2, 5],
        2: [1, 2, 3, 6],
        3: [2, 3, 4, 7],
        4: [3, 4, 8],
        5: [1, 5, 6, 9],
        6: [2, 5, 6, 7, 10],
        7: [3, 6, 7, 8],
         8: [4, 7, 8],
        9: [5, 9, 10],
        10: [6, 9, 10]
    }

    for h in hexagons[key]:
        lights[h-1] = 1 - lights[h-1]  # Inverte o estado da luz


# Leitura da configuração inicial do painel de luzes
lights = list(map(int, input().split()))

# Chamada da função para pressionar as teclas e obter a menor sequência
min_moves, min_sequence = press_keys(lights)

# Impressão do resultado
print(min_moves)
if min_moves != -1:
    print(min_sequence.strip())
