# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def build_totients(limit):
    phi = [i for i in range(limit + 1)]
    for prime in range(2, limit + 1):
        if phi[prime] == prime:
            step = prime
            for value in range(prime, limit + 1, step):
                phi[value] -= phi[value] // prime
    return phi

def main():
    raw = sys.stdin.buffer.read().split()
    if not raw:
        return
    nums = [int(x) for x in raw]
    total = nums[0]
    jobs = []
    high = 0
    at = 1
    for _ in range(total):
        n = nums[at]
        k = nums[at + 1]
        at += 2
        jobs.append((n, k))
        high = max(high, n)

    phi = build_totients(high)
    pair_count = [0] * (high + 1)
    for i in range(1, high + 1):
        pair_count[i] = pair_count[i - 1] + phi[i]

    width = high + 1
    table = [0] * ((high + 2) * width)
    for right in range(1, high + 1):
        for left in range(right, 0, -1):
            table[left * width + right] = table[(left + 1) * width + right] + pair_count[right // left]

    answers = []
    big = 10 ** 32
    for n, k in jobs:
        groups = min(k, n)
        previous = [0] * (n + 1)
        for end in range(1, n + 1):
            previous[end] = table[width + end]

        for used in range(2, groups + 1):
            current = [0] * (n + 1)
            stack = [(used, n, used - 1, n - 1)]
            while stack:
                left, right, opt_l, opt_r = stack.pop()
                if left > right:
                    continue
                mid = (left + right) >> 1
                best_value = big
                best_cut = opt_l
                last = opt_r
                if last >= mid:
                    last = mid - 1
                for cut in range(opt_l, last + 1):
                    candidate = previous[cut] + table[(cut + 1) * width + mid]
                    if candidate < best_value:
                        best_value = candidate
                        best_cut = cut
                current[mid] = best_value
                stack.append((mid + 1, right, best_cut, opt_r))
                stack.append((left, mid - 1, opt_l, best_cut))
            previous = current
        answers.append(str(previous[n]))

# CLAUSE: finish_program
    sys.stdout.write("\n".join(answers))

if __name__ == "__main__":
    main()
