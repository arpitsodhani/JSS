# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def hypergeom_terms(alive, total, take):
    lo = max(0, take - (total - alive))
    hi = min(alive, take)

    if alive == 0 or lo == hi:
        return [(lo, 1.0)]

    pivot = ((take + 1) * (alive + 1)) // (total + 2)
    pivot = min(hi, max(lo, pivot))

    left = []
    right = [(pivot, 1.0)]
    total_weight = 1.0

    weight = 1.0
    x = pivot - 1
    while x >= lo:
        weight *= (x + 1) * (total - alive - take + x + 1)
        weight /= (alive - x) * (take - x)
        left.append((x, weight))
        total_weight += weight
        x -= 1

    weight = 1.0
    for x in range(pivot + 1, hi + 1):
        prev = x - 1
        weight *= (alive - prev) * (take - prev)
        weight /= x * (total - alive - take + x)
        right.append((x, weight))
        total_weight += weight

    return [(x, w / total_weight) for x, w in left + right]

def consume(dist, total, take):
    length = len(dist)
    if take == 0:
        return dist[:]
    if take == total:
        answer = [0.0] * length
        answer[0] = 1.0
        return answer

    answer = [0.0] * length
    nonzero = [(alive, prob) for alive, prob in enumerate(dist) if prob != 0.0]
    for alive, prob in nonzero:
        for chosen, chance in hypergeom_terms(alive, total, take):
            answer[alive - chosen] += prob * chance
    return answer

def run():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    n = numbers[0]
    pots = [0] + numbers[1:1 + n]
    q_index = 1 + n
    q = numbers[q_index]
    query_index = q_index + 1

    dist = [None]
    empty = [0.0] * (n + 1)
    expected = 0.0

    for amount in pots[1:]:
        row = [0.0] * (amount + 1)
        row[amount] = 1.0
        dist.append(row)

    for i in range(1, n + 1):
        if pots[i] == 0:
            empty[i] = 1.0
            expected += 1.0

    result = []
    end = query_index + 3 * q
    while query_index < end:
        u = numbers[query_index]
        v = numbers[query_index + 1]
        k = numbers[query_index + 2]
        query_index += 3

        previous_empty = empty[u]
        dist[u] = consume(dist[u], pots[u], k)
        empty[u] = dist[u][0]
        expected += empty[u] - previous_empty

        if u != v:
            pots[u] -= k
            pots[v] += k

        result.append(f"{expected:.12f}")

    return "\n".join(result)

def main():
    sys.stdout.write(run())

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
