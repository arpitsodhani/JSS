# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys

    def solve():
        data = sys.stdin.read().split()
        if not data:
            return

        t = int(data[0])
        idx = 1
        ans = []

        for _ in range(t):
            n = int(data[idx])
            s = data[idx + 1].strip()
            idx += 2

            pref = [0] * (n + 1)
            cur = 0
            for i, ch in enumerate(s, 1):
                cur += 1 if ch == '1' else -1
                pref[i] = cur

            pref.sort()
            total_abs = 0
            prefix_sum = 0
            for i, x in enumerate(pref):
                total_abs += x * i - prefix_sum
                prefix_sum += x

            total_len = n * (n + 1) * (n + 2) // 6
            ans.append(str((total_len + total_abs) // 2))

        sys.stdout.write("\n".join(ans))

    if __name__ == "__main__":
        solve()

# CLAUSE: finish_program
def main():
    _inner_main()

main()
