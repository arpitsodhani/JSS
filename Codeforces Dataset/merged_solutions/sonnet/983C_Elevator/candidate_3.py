# CLAUSE: setup_environment
import sys
from heapq import heappop, heappush

def main():
    values = list(map(int, sys.stdin.buffer.read().split()))
    if not values:
        return
    n = values[0]
    people = [(values[i], values[i + 1]) for i in range(1, 2 * n + 1, 2)]

# CLAUSE: solve_logic
    start = (0, 1, (0, 0, 0, 0, 0, 0, 0, 0, 0, 0))
    heap = [(0, start)]
    best = {start: 0}
    result = 0

    while heap:
        spent, state = heappop(heap)
        if best.get(state) != spent:
            continue

        index, floor, inside = state
        if index == n and sum(inside) == 0:
            result = spent
            break

        occupied = sum(inside)

        for target in range(1, 10):
            leaving = inside[target]
            if leaving == 0:
                continue
            changed = list(inside)
            changed[target] = 0
            load = occupied - leaving
            nxt = index
            entered = 0
            while nxt < n and load < 4 and people[nxt][0] == target:
                changed[people[nxt][1]] += 1
                load += 1
                entered += 1
                nxt += 1
            packed = tuple(changed)
            new_state = (nxt, target, packed)
            new_spent = spent + abs(floor - target) + leaving + entered
            if new_spent < best.get(new_state, 10 ** 30):
                best[new_state] = new_spent
                heappush(heap, (new_spent, new_state))

        if index < n:
            target = people[index][0]
            if inside[target] == 0 and occupied < 4:
                changed = list(inside)
                load = occupied
                nxt = index
                entered = 0
                while nxt < n and load < 4 and people[nxt][0] == target:
                    changed[people[nxt][1]] += 1
                    load += 1
                    entered += 1
                    nxt += 1
                packed = tuple(changed)
                new_state = (nxt, target, packed)
                new_spent = spent + abs(floor - target) + entered
                if new_spent < best.get(new_state, 10 ** 30):
                    best[new_state] = new_spent
                    heappush(heap, (new_spent, new_state))

# CLAUSE: finish_program
    print(result)

if __name__ == "__main__":
    main()
