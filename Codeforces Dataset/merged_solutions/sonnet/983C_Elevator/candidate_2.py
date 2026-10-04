# CLAUSE: setup_environment
import sys
from heapq import heappop, heappush

def build_codes(pos, left, value, weights, out):
    if pos == 10:
        out.append(value)
        return
    for amount in range(left + 1):
        build_codes(pos + 1, left - amount, value + amount * weights[pos], weights, out)

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n = data[0]
    starts = [0] * n
    ends = [0] * n
    p = 1
    for i in range(n):
        starts[i] = data[p]
        ends[i] = data[p + 1]
        p += 2

# CLAUSE: solve_logic
    weights = [0] * 10
    weights[1] = 1
    for i in range(2, 10):
        weights[i] = weights[i - 1] * 5
    modulus = weights[9] * 5

    all_codes = []
    build_codes(1, 4, 0, weights, all_codes)

    load_size = {}
    destinations = {}
    without_count = {}
    without_code = {}
    for code in all_codes:
        size = 0
        active = []
        counts = [0] * 10
        dropped = [0] * 10
        for floor in range(1, 10):
            count = (code // weights[floor]) % 5
            counts[floor] = count
            dropped[floor] = code - count * weights[floor]
            size += count
            if count:
                active.append(floor)
        load_size[code] = size
        destinations[code] = active
        without_count[code] = counts
        without_code[code] = dropped

    def pack(person, floor, code):
        return ((person * 9 + floor - 1) * modulus + code)

    pq = [(0, pack(0, 1, 0))]
    dist = {pack(0, 1, 0): 0}
    answer = None

    while pq:
        cost, key = heappop(pq)
        if dist.get(key) != cost:
            continue

        code = key % modulus
        rest = key // modulus
        floor = rest % 9 + 1
        person = rest // 9

        if person == n and code == 0:
            answer = cost
            break

        for target in destinations[code]:
            removed = without_count[code][target]
            next_code = without_code[code][target]
            load = load_size[next_code]
            nxt = person
            entered = 0
            while nxt < n and load < 4 and starts[nxt] == target:
                next_code += weights[ends[nxt]]
                load += 1
                entered += 1
                nxt += 1
            new_cost = cost + abs(floor - target) + removed + entered
            new_key = pack(nxt, target, next_code)
            if new_cost < dist.get(new_key, 10 ** 30):
                dist[new_key] = new_cost
                heappush(pq, (new_cost, new_key))

        if person < n:
            target = starts[person]
            if without_count[code][target] == 0 and load_size[code] < 4:
                next_code = code
                load = load_size[code]
                nxt = person
                entered = 0
                while nxt < n and load < 4 and starts[nxt] == target:
                    next_code += weights[ends[nxt]]
                    load += 1
                    entered += 1
                    nxt += 1
                new_cost = cost + abs(floor - target) + entered
                new_key = pack(nxt, target, next_code)
                if new_cost < dist.get(new_key, 10 ** 30):
                    dist[new_key] = new_cost
                    heappush(pq, (new_cost, new_key))

# CLAUSE: finish_program
    print(answer)

if __name__ == "__main__":
    main()
