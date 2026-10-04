# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _run_case_program():
    import sys

    def main():
        data = list(map(int, sys.stdin.read().split()))
        if not data:
            return

        n, m = data[0], data[1]
        c = data[2:2 + n]

        cnt = [0] * (m + 1)
        for x in c:
            cnt[x] += 1

        colors = []
        max_cnt = 0
        for i in range(1, m + 1):
            if cnt[i]:
                max_cnt = max(max_cnt, cnt[i])
                colors.append((cnt[i], i))

        colors.sort(reverse=True)

        a = []
        for count, color in colors:
            a.extend([color] * count)

        shift = max_cnt
        good = n - max(0, 2 * max_cnt - n)

        out = [str(good)]
        for i in range(n):
            out.append(f"{a[i]} {a[(i + shift) % n]}")

        sys.stdout.write("\n".join(out))

    if __name__ == "__main__":
        main()

# CLAUSE: finish_program
if __name__ == "__main__":
    _run_case_program()
