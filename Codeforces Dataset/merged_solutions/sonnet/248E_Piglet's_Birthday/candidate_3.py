# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def distribution_after_tasting(dist, total_count, picked_count):
    size = len(dist)
    if picked_count == 0:
        return dist.copy()
    if picked_count == total_count:
        nxt = [0.0] * size
        nxt[0] = 1.0
        return nxt

    nxt = [0.0] * size
    for alive_count in range(size):
        base = dist[alive_count]
        if base == 0.0:
            continue

        smallest = picked_count - (total_count - alive_count)
        if smallest < 0:
            smallest = 0
        largest = alive_count if alive_count < picked_count else picked_count

        if alive_count == 0 or smallest == largest:
            nxt[alive_count - smallest] += base
            continue

        center = ((picked_count + 1) * (alive_count + 1)) // (total_count + 2)
        if center < smallest:
            center = smallest
        if center > largest:
            center = largest

        chosen_values = [center]
        weights = [1.0]
        weight_sum = 1.0

        weight = 1.0
        for x in range(center - 1, smallest - 1, -1):
            weight = weight * (x + 1) * (total_count - alive_count - picked_count + x + 1)
            weight = weight / ((alive_count - x) * (picked_count - x))
            chosen_values.append(x)
            weights.append(weight)
            weight_sum += weight

        weight = 1.0
        x = center + 1
        while x <= largest:
            y = x - 1
            weight = weight * (alive_count - y) * (picked_count - y)
            weight = weight / (x * (total_count - alive_count - picked_count + x))
            chosen_values.append(x)
            weights.append(weight)
            weight_sum += weight
            x += 1

        multiplier = base / weight_sum
        for i in range(len(chosen_values)):
            nxt[alive_count - chosen_values[i]] += multiplier * weights[i]

    return nxt

def solve(data):
    it = iter(data)
    n = next(it)
    counts = [0]
    for _ in range(n):
        counts.append(next(it))
    q = next(it)

    probabilities = [[] for _ in range(n + 1)]
    empty_probability = [0.0] * (n + 1)
    expected = 0.0

    for i, count in enumerate(counts[1:], 1):
        row = [0.0] * (count + 1)
        row[count] = 1.0
        probabilities[i] = row
        if count == 0:
            empty_probability[i] = 1.0
            expected += 1.0

    lines = []
    for _ in range(q):
        u = next(it)
        v = next(it)
        k = next(it)

        old = empty_probability[u]
        probabilities[u] = distribution_after_tasting(probabilities[u], counts[u], k)
        now = probabilities[u][0]
        empty_probability[u] = now
        expected += now - old

        if u != v:
            counts[u] -= k
            counts[v] += k

        lines.append(f"{expected:.12f}")

    return "\n".join(lines)

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    sys.stdout.write(solve(data))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
