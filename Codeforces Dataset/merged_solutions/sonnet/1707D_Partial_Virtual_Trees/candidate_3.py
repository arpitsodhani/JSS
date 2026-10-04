# CLAUSE: setup_environment
import sys
from array import array

# CLAUSE: solve_logic
def build_node(parts, limit, mod):
    if not parts:
        return array("I", [0] + [x % mod for x in range(1, limit + 1)])
    if len(parts) == 1:
        source = parts[0]
        ans = array("I", [0]) * (limit + 1)
        for x in range(1, limit + 1):
            ans[x] = x * source[x] % mod
        return ans

    cnt = len(parts)
    ans = array("I", [0]) * (limit + 1)
    left = [1] * (cnt + 1)
    carry = [0] * cnt
    all_sum = 0
    adjust = (1 - cnt) % mod

    for x in range(1, limit + 1):
        i = 0
        while i < cnt:
            left[i + 1] = left[i] * parts[i][x] % mod
            i += 1
        all_sum = (all_sum + left[cnt]) % mod

        right = 1
        val_sum = 0
        i = cnt - 1
        while i >= 0:
            value = parts[i][x]
            other = left[i] * right % mod
            carry[i] = (carry[i] + other) % mod
            val_sum = (val_sum + value * carry[i]) % mod
            right = right * value % mod
            i -= 1
        ans[x] = (val_sum + adjust * all_sum) % mod
    return ans

def main():
    raw = sys.stdin.buffer.read().split()
    if not raw:
        return
    values = list(map(int, raw))
    n = values[0]
    p = values[1]
    limit = n - 1
    if limit == 0:
        sys.stdout.write("\n")
        return

    graph = [[] for _ in range(n + 1)]
    pos = 2
    for _ in range(limit):
        u = values[pos]
        v = values[pos + 1]
        pos += 2
        graph[u].append(v)
        graph[v].append(u)

    parent = [-2] * (n + 1)
    parent[1] = 0
    sequence = [1]
    for node in sequence:
        for nxt in graph[node]:
            if parent[nxt] == -2:
                parent[nxt] = node
                sequence.append(nxt)

    buckets = [[] for _ in range(n + 1)]
    result_at_root = None

    for node in reversed(sequence):
        child_values = buckets[node]
        if node == 1:
            result_at_root = array("I", [1]) * (limit + 1)
            for arr in child_values:
                for x in range(limit + 1):
                    result_at_root[x] = result_at_root[x] * arr[x] % p
        else:
            made = build_node(child_values, limit, p)
            buckets[parent[node]].append(made)

    c = [0] * (limit + 1)
    c[0] = 1
    answer = []
    for k in range(1, limit + 1):
        for j in range(k, 0, -1):
            c[j] = (c[j] + c[j - 1]) % p
        total = 0
        for s in range(k + 1):
            if (k - s) & 1:
                total -= c[s] * result_at_root[s]
            else:
                total += c[s] * result_at_root[s]
        answer.append(str(total % p))
    print(" ".join(answer))

# CLAUSE: finish_program
main()
