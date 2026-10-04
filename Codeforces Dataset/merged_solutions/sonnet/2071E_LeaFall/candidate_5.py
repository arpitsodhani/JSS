# CLAUSE: setup_environment
import sys

P = 998244353
INV_TWO = 499122177

# CLAUSE: solve_logic
def answer_case(n, pq, links):
    down = [0] * (n + 1)
    up = [0] * (n + 1)
    reciprocal = [0] * (n + 1)

    for vertex in range(1, n + 1):
        p, q = pq[vertex - 1]
        d = (p % P) * pow(q % P, P - 2, P) % P
        down[vertex] = d
        up[vertex] = (1 - d) % P
        if d != 0:
            reciprocal[vertex] = pow(d, P - 2, P)

    neighbors = [[] for _ in range(n + 1)]
    for left, right in links:
        neighbors[left].append(right)
        neighbors[right].append(left)

    zero_neighbors = [0] * (n + 1)
    fall_product = [1] * (n + 1)
    weighted_sum = [0] * (n + 1)

    for vertex, row in enumerate(neighbors):
        if vertex == 0:
            continue
        zp = 0
        fp = 1
        ws = 0
        for other in row:
            if down[other] == 0:
                zp += 1
            else:
                fp = fp * down[other] % P
                ws = (ws + up[other] * reciprocal[other]) % P
        zero_neighbors[vertex] = zp
        fall_product[vertex] = fp
        weighted_sum[vertex] = ws

    def exclude(vertex, blocked):
        if down[blocked] == 0:
            return zero_neighbors[vertex] - 1, fall_product[vertex], weighted_sum[vertex]
        return zero_neighbors[vertex], fall_product[vertex] * reciprocal[blocked] % P, (weighted_sum[vertex] - up[blocked] * reciprocal[blocked]) % P

    def exact_one_from(z, product, total):
        if z == 0:
            return product * total % P
        if z == 1:
            return product
        return 0

    leaf_probability = [0] * (n + 1)
    sum_leaf = 0
    sum_leaf_square = 0

    for vertex in range(1, n + 1):
        chance = up[vertex] * exact_one_from(zero_neighbors[vertex], fall_product[vertex], weighted_sum[vertex]) % P
        leaf_probability[vertex] = chance
        sum_leaf = (sum_leaf + chance) % P
        sum_leaf_square = (sum_leaf_square + chance * chance) % P

    total_answer = (sum_leaf * sum_leaf - sum_leaf_square) * INV_TWO % P

    for left, right in links:
        zl, pl, _ = exclude(left, right)
        zr, pr, _ = exclude(right, left)
        both = 0
        if zl == 0 and zr == 0:
            both = up[left] * up[right] % P * pl % P * pr % P
        total_answer = (total_answer + both - leaf_probability[left] * leaf_probability[right]) % P

    for center in range(1, n + 1):
        first_sum = first_square = 0
        second_sum = second_square = 0
        independent_sum = independent_square = 0

        for child in neighbors[center]:
            z, product, total = exclude(child, center)
            all_fall = product if z == 0 else 0
            one_alive = exact_one_from(z, product, total)
            first = up[child] * all_fall % P
            second = up[child] * one_alive % P
            independent = leaf_probability[child]

            first_sum = (first_sum + first) % P
            first_square = (first_square + first * first) % P
            second_sum = (second_sum + second) % P
            second_square = (second_square + second * second) % P
            independent_sum = (independent_sum + independent) % P
            independent_square = (independent_square + independent * independent) % P

        real_pairs = up[center] * (first_sum * first_sum - first_square)
        real_pairs = (real_pairs + down[center] * (second_sum * second_sum - second_square)) % P
        real_pairs = real_pairs * INV_TWO % P
        fake_pairs = (independent_sum * independent_sum - independent_square) * INV_TWO % P
        total_answer = (total_answer + real_pairs - fake_pairs) % P

    return total_answer % P

# CLAUSE: finish_program
def main():
    values = list(map(int, sys.stdin.buffer.read().split()))
    index = 0
    tests = values[index]
    index += 1
    lines = []

    for _ in range(tests):
        n = values[index]
        index += 1

        pq = []
        for _ in range(n):
            pq.append((values[index], values[index + 1]))
            index += 2

        links = []
        for _ in range(n - 1):
            links.append((values[index], values[index + 1]))
            index += 2

        lines.append(str(answer_case(n, pq, links)))

    sys.stdout.write("\n".join(lines))

if __name__ == "__main__":
    main()
