# CLAUSE: setup_environment
import sys
from collections import Counter

MOD = 1000000007

def build_lucky_numbers(limit):
    result = set()
    stack = [4, 7]
    while stack:
        x = stack.pop()
        if x > limit:
            continue
        result.add(x)
        stack.append(x * 10 + 4)
        stack.append(x * 10 + 7)
    return result

# CLAUSE: solve_logic
def main():
    data = [int(x) for x in sys.stdin.buffer.read().split()]
    n, k = data[0], data[1]
    arr = data[2:]
    lucky_set = build_lucky_numbers(max(arr) if arr else 0)

    counts = Counter()
    free_count = 0
    for x in arr:
        if x in lucky_set:
            counts[x] += 1
        else:
            free_count += 1

    combinations = [[0] * (k + 1) for _ in range(free_count + 1)]
    combinations[0][0] = 1
    for i in range(1, free_count + 1):
        combinations[i][0] = 1
        upto = min(i, k)
        for j in range(1, upto + 1):
            combinations[i][j] = (combinations[i - 1][j - 1] + combinations[i - 1][j]) % MOD

    ways = [0] * (len(counts) + 1)
    ways[0] = 1
    highest = 0
    for amount in counts.values():
        nxt = ways[:]
        for selected in range(highest + 1):
            nxt[selected + 1] = (nxt[selected + 1] + ways[selected] * amount) % MOD
        ways = nxt
        highest += 1

    answer = 0
    for selected in range(min(k, len(counts)) + 1):
        need = k - selected
        if need <= free_count:
            answer = (answer + ways[selected] * combinations[free_count][need]) % MOD
    print(answer)

# CLAUSE: finish_program
main()
