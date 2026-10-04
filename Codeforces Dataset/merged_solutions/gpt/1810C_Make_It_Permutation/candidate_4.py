# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys

    def main():
        data = list(map(int, sys.stdin.buffer.read().split()))
        t = data[0]
        idx = 1
        ans = []

        for _ in range(t):
            n = data[idx]
            c = data[idx + 1]
            d = data[idx + 2]
            idx += 3

            a = data[idx:idx + n]
            idx += n

            b = sorted(set(a))
            k = len(b)
            duplicates = n - k

            best = n * c + d

            for i, x in enumerate(b, 1):
                cost = duplicates * c + (k - i) * c + (x - i) * d
                if cost < best:
                    best = cost

            ans.append(str(best))

        sys.stdout.write("\n".join(ans))

    if __name__ == "__main__":
        main()

# CLAUSE: finish_program
def main():
    _inner_main()

main()
