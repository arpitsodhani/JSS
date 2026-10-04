# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    idx = 1
    out = []

    for _ in range(t):
        n = int(data[idx])
        m = int(data[idx + 1])
        idx += 2

        x = list(map(int, data[idx:idx + n]))
        idx += n

        rows = [data[idx + i].decode() for i in range(n)]
        idx += n

        colmask = [0] * m
        for i, s in enumerate(rows):
            bit = 1 << i
            for j, ch in enumerate(s):
                if ch == '1':
                    colmask[j] |= bit

        lim = 1 << n
        sign_sum = [0] * lim
        const = [0] * lim

        for mask in range(lim):
            ss = 0
            cs = 0
            for i in range(n):
                if mask >> i & 1:
                    ss += 1
                    cs += x[i]
                else:
                    ss -= 1
                    cs -= x[i]
            sign_sum[mask] = ss
            const[mask] = cs

        best_val = None
        best_perm = None

        for mask in range(lim):
            vals = []
            total = const[mask]

            for j, cm in enumerate(colmask):
                inter = (mask & cm).bit_count()
                ones = cm.bit_count()
                d = 2 * inter - ones
                vals.append((d, j))

            vals.sort()
            perm = [0] * m

            for k, (d, j) in enumerate(vals):
                p = m - k
                perm[j] = p
                total -= p * d

            if best_val is None or total > best_val:
                best_val = total
                best_perm = perm

        out.append(" ".join(map(str, best_perm)))

    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
