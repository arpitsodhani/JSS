# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys

    def main():
        data = list(map(int, sys.stdin.buffer.read().split()))
        idx = 0
        t = data[idx]
        idx += 1
        out = []

        for _ in range(t):
            n = data[idx]
            q = data[idx + 1]
            idx += 2

            arr = data[idx:idx + n]
            idx += n

            pref_sum = [0] * (n + 1)
            pref_one = [0] * (n + 1)

            for i, x in enumerate(arr, 1):
                pref_sum[i] = pref_sum[i - 1] + x
                pref_one[i] = pref_one[i - 1] + (1 if x == 1 else 0)

            for _ in range(q):
                l = data[idx]
                r = data[idx + 1]
                idx += 2

                length = r - l + 1
                total = pref_sum[r] - pref_sum[l - 1]
                ones = pref_one[r] - pref_one[l - 1]

                if length > 1 and total >= length + ones:
                    out.append("YES")
                else:
                    out.append("NO")

        sys.stdout.write("\n".join(out))

    if __name__ == "__main__":
        main()

# CLAUSE: finish_program
def main():
    _inner_main()

main()
