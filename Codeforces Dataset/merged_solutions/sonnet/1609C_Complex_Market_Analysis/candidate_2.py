# CLAUSE: setup_environment
import sys

def prime_table(limit):
    prime = [True] * (limit + 1)
    if limit >= 0:
        prime[0] = False
    if limit >= 1:
        prime[1] = False
    d = 2
    while d * d <= limit:
        if prime[d]:
            step_start = d * d
            prime[step_start:limit + 1:d] = [False] * (((limit - step_start) // d) + 1)
        d += 1
    return prime

# CLAUSE: solve_logic
def solve():
    nums = list(map(int, sys.stdin.buffer.read().split()))
    t = nums[0]
    p = 1
    cases = []
    largest = 0
    for _ in range(t):
        n = nums[p]
        e = nums[p + 1]
        p += 2
        arr = nums[p:p + n]
        p += n
        cases.append((n, e, arr))
        current = max(arr)
        if current > largest:
            largest = current

    is_prime = prime_table(largest)
    out = []

    for n, e, arr in cases:
        total = 0
        for r in range(e):
            seq = arr[r:n:e]
            length = len(seq)
            left = [0] * length
            streak = 0
            for i, value in enumerate(seq):
                if value == 1:
                    streak += 1
                else:
                    streak = 0
                left[i] = streak

            right = [0] * length
            streak = 0
            for i in range(length - 1, -1, -1):
                if seq[i] == 1:
                    streak += 1
                else:
                    streak = 0
                right[i] = streak

            for i, value in enumerate(seq):
                if is_prime[value]:
                    a = left[i - 1] if i else 0
                    b = right[i + 1] if i + 1 < length else 0
                    total += (a + 1) * (b + 1) - 1
        out.append(str(total))
    return "\n".join(out)

# CLAUSE: finish_program
if __name__ == "__main__":
    sys.stdout.write(solve())
