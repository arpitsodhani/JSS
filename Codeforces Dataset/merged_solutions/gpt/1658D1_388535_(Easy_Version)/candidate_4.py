# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys

    def count_ones_upto(n, b):
        if n < 0:
            return 0
        cycle = 1 << (b + 1)
        full = (n + 1) // cycle
        rem = (n + 1) % cycle
        return full * (1 << b) + max(0, rem - (1 << b))

    def count_ones_range(l, r, b):
        return count_ones_upto(r, b) - count_ones_upto(l - 1, b)

    def main():
        data = list(map(int, sys.stdin.buffer.read().split()))
        t = data[0]
        idx = 1
        ans = []
        for _ in range(t):
            l, r = data[idx], data[idx + 1]
            idx += 2
            n = r - l + 1
            a = data[idx:idx + n]
            idx += n

            x = 0
            for b in range(18):
                ca = sum((v >> b) & 1 for v in a)
                cr = count_ones_range(l, r, b)
                if ca != cr:
                    x |= 1 << b

            ans.append(str(x))
        print("\n".join(ans))

    if __name__ == "__main__":
        main()

# CLAUSE: finish_program
def main():
    _inner_main()

main()
