# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _run_case_program():
    import sys

    def main():
        data = list(map(int, sys.stdin.buffer.read().split()))
        t = data[0]
        idx = 1
        out = []

        for _ in range(t):
            n = data[idx]
            k = data[idx + 1]
            idx += 2

            a = data[idx:idx + n]
            idx += n

            p = data[idx:idx + k]
            idx += k

            x = a[p[0] - 1]
            cnt = [0] * (k + 1)

            j = 0
            prev = 0
            total = 0

            for pos in range(1, n + 2):
                cur = (a[pos - 1] ^ x) if pos <= n else 0

                if cur != prev:
                    while j < k and p[j] < pos:
                        j += 1
                    cnt[j] += 1
                    total += 1

                prev = cur

            base = total // 2
            mx = max(cnt)
            out.append(str(base + max(0, mx - base)))

        sys.stdout.write("\n".join(out))

    if __name__ == "__main__":
        main()

# CLAUSE: finish_program
if __name__ == "__main__":
    _run_case_program()
