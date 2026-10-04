# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def move_update(state, total, take):
    limit = len(state) - 1
    if take == 0:
        return state[:]
    if take == total:
        result = [0.0] * (limit + 1)
        result[0] = 1.0
        return result

    result = [0.0] * (limit + 1)
    for alive, probability in enumerate(state):
        if probability == 0.0:
            continue
        if alive == 0:
            result[0] += probability
            continue

        low = max(0, take - (total - alive))
        high = min(alive, take)
        if low == high:
            result[alive - low] += probability
            continue

        mode = ((take + 1) * (alive + 1)) // (total + 2)
        mode = max(low, min(high, mode))

        terms = [(mode, 1.0)]
        total_weight = 1.0

        weight = 1.0
        chosen = mode - 1
        while chosen >= low:
            weight *= (chosen + 1) * (total - alive - take + chosen + 1)
            weight /= (alive - chosen) * (take - chosen)
            terms.append((chosen, weight))
            total_weight += weight
            chosen -= 1

        weight = 1.0
        for chosen in range(mode + 1, high + 1):
            previous = chosen - 1
            weight *= (alive - previous) * (take - previous)
            weight /= chosen * (total - alive - take + chosen)
            terms.append((chosen, weight))
            total_weight += weight

        factor = probability / total_weight
        for chosen, weight in terms:
            result[alive - chosen] += factor * weight

    return result

def main():
    values = list(map(int, sys.stdin.buffer.read().split()))
    pos = 0
    n = values[pos]
    pos += 1
    pots = [0] + values[pos:pos + n]
    pos += n
    q = values[pos]
    pos += 1

    states = [None] * (n + 1)
    empty = [0.0] * (n + 1)
    answer = 0.0

    for shelf in range(1, n + 1):
        count = pots[shelf]
        states[shelf] = [0.0] * (count + 1)
        states[shelf][count] = 1.0
        if count == 0:
            empty[shelf] = 1.0
            answer += 1.0

    output = []
    for _ in range(q):
        u, v, k = values[pos], values[pos + 1], values[pos + 2]
        pos += 3

        before = empty[u]
        states[u] = move_update(states[u], pots[u], k)
        empty[u] = states[u][0]
        answer += empty[u] - before

        if u != v:
            pots[u] -= k
            pots[v] += k

        output.append("%.12f" % answer)

    sys.stdout.write("\n".join(output))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
