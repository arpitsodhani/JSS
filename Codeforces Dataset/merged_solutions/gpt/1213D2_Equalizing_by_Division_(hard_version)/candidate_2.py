# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n, k = (data[0], data[1])
    a = data[2:]
    max_v = max(a) if a else 0
    costs = [[] for _ in range(max_v + 1)]
    for x in a:
        steps = 0
        while True:
            costs[x].append(steps)
            if x == 0:
                break
            x //= 2
            steps += 1
    ans = 10 ** 18
    for lst in costs:
        if len(lst) >= k:
            lst.sort()
            s = sum(lst[:k])
            if s < ans:
                ans = s
    print(ans)
if __name__ == '__main__':
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = 0
