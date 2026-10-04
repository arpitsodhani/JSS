# Clause setup_environment [Confidence: 0.60]
import sys
from heapq import heappop, heappush

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n = data[0]
    starts = [data[i] for i in range(1, 2 * n + 1, 2)]
    ends = [data[i] for i in range(2, 2 * n + 1, 2)]


# Clause solve_logic [Confidence: 0.60]
    place = [0] * 10
    place[1] = 1
    for floor in range(2, 10):
        place[floor] = place[floor - 1] * 5
    base = place[9] * 5

    states = [0]
    for floor in range(1, 10):
        next_states = []
        step = place[floor]
        for code in states:
            for add in range(5):
                next_states.append(code + add * step)
        states = next_states

    total = [0] * base
    floors = [[] for _ in range(base)]
    count_at = [[0] * 10 for _ in range(base)]
    erased = [[0] * 10 for _ in range(base)]

    for code in states:
        s = 0
        seen = []
        for floor in range(1, 10):
            c = (code // place[floor]) % 5
            count_at[code][floor] = c
            erased[code][floor] = code - c * place[floor]
            s += c
            if c:
                seen.append(floor)
        if s <= 4:
            total[code] = s
            floors[code] = seen

    def encode(index, floor, code):
        return ((index * 9 + floor - 1) * base + code)

    def board(index, floor, code, load):
        got = 0
        while index < n and load < 4 and starts[index] == floor:
            code += place[ends[index]]
            index += 1
            load += 1
            got += 1
        return index, code, got

    initial = encode(0, 1, 0)
    dist = {initial: 0}
    heap = [(0, initial)]
    final_answer = 0

    while heap:
        current, packed = heappop(heap)
        if current != dist.get(packed):
            continue

        code = packed % base
        left = packed // base
        floor = left % 9 + 1
        index = left // 9

        if index == n and code == 0:
            final_answer = current
            break

        moves = floors[code][:]
        if index < n and count_at[code][starts[index]] == 0 and total[code] < 4:
            moves.append(starts[index])

        for target in moves:
            out = count_at[code][target]
            reduced = erased[code][target] if out else code
            load = total[code] - out
            next_index, next_code, entered = board(index, target, reduced, load)
            candidate = current + abs(floor - target) + out + entered
            token = encode(next_index, target, next_code)
            if candidate < dist.get(token, 10 ** 30):
                dist[token] = candidate
                heappush(heap, (candidate, token))


# Clause finish_program [Confidence: 0.80]
    print(answer)

if __name__ == "__main__":
    main()


