# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    content = sys.stdin.buffer.read()
    if not content:
        return
    values = [int(x) for x in content.split()]
    q = values[0]
    pairs = [(values[i], values[i + 1]) for i in range(1, 2 * q + 1, 2)]
    max_n = 0
    for n, _ in pairs:
        if n > max_n:
            max_n = n

    phi = [0] * (max_n + 1)
    for i in range(max_n + 1):
        phi[i] = i
    for i in range(2, max_n + 1):
        if phi[i] == i:
            reduced = i - 1
            phi[i] = reduced
            for j in range(i + i, max_n + 1, i):
                phi[j] -= phi[j] // i

    cop = [0] * (max_n + 1)
    running = 0
    for i in range(1, max_n + 1):
        running += phi[i]
        cop[i] = running

    cost = [[0] * (max_n + 1) for _ in range(max_n + 2)]
    for left in range(max_n, 0, -1):
        row = cost[left]
        below = cost[left + 1]
        right = left
        while right <= max_n:
            row[right] = below[right] + cop[right // left]
            right += 1

    ans = []
    infinity = 10 ** 30

    for n, k in pairs:
        pieces = k if k < n else n
        old = [0] * (n + 1)
        for end in range(1, n + 1):
            old[end] = cost[1][end]

        part = 2
        while part <= pieces:
            new = [0] * (n + 1)
            ranges = [(part, n, part - 1, n - 1)]
            while ranges:
                lo, hi, opt_lo, opt_hi = ranges.pop()
                if lo <= hi:
                    mid = (lo + hi) // 2
                    best_cut = opt_lo
                    best_score = infinity
                    limit = min(opt_hi, mid - 1)
                    for split in range(opt_lo, limit + 1):
                        score = old[split] + cost[split + 1][mid]
                        if score < best_score:
                            best_score = score
                            best_cut = split
                    new[mid] = best_score
                    if lo < mid:
                        ranges.append((lo, mid - 1, opt_lo, best_cut))
                    if mid < hi:
                        ranges.append((mid + 1, hi, best_cut, opt_hi))
            old = new
            part += 1

        ans.append(str(old[n]))

# CLAUSE: finish_program
    sys.stdout.write("\n".join(ans))

if __name__ == "__main__":
    main()
