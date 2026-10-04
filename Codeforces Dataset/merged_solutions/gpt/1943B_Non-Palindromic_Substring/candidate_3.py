# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _run_case_program():
    import sys

    def manacher(s):
        n = len(s)
        d1 = [0] * n
        l = 0
        r = -1
        for i in range(n):
            k = 1 if i > r else min(d1[l + r - i], r - i + 1)
            while i - k >= 0 and i + k < n and s[i - k] == s[i + k]:
                k += 1
            d1[i] = k
            if i + k - 1 > r:
                l = i - k + 1
                r = i + k - 1

        d2 = [0] * n
        l = 0
        r = -1
        for i in range(n):
            k = 0 if i > r else min(d2[l + r - i + 1], r - i + 1)
            while i - k - 1 >= 0 and i + k < n and s[i - k - 1] == s[i + k]:
                k += 1
            d2[i] = k
            if i + k - 1 > r:
                l = i - k
                r = i + k - 1

        return d1, d2

    def is_pal(l, r, d1, d2):
        length = r - l + 1
        if length & 1:
            c = (l + r) // 2
            return d1[c] >= length // 2 + 1
        c = (l + r + 1) // 2
        return d2[c] >= length // 2

    def solve():
        data = sys.stdin.buffer.read().split()
        if not data:
            return

        t = int(data[0])
        idx = 1
        out = []

        for _ in range(t):
            n = int(data[idx])
            q = int(data[idx + 1])
            idx += 2
            s = data[idx].decode()
            idx += 1

            d1, d2 = manacher(s)

            same_pref = [0] * n
            for i in range(n - 1):
                same_pref[i + 1] = same_pref[i] + (s[i] != s[i + 1])

            alt_pref = [0] * max(1, n - 1)
            for i in range(n - 2):
                alt_pref[i + 1] = alt_pref[i] + (s[i] != s[i + 2])

            for _ in range(q):
                l = int(data[idx]) - 1
                r = int(data[idx + 1]) - 1
                idx += 2

                m = r - l + 1
                total = m * (m + 1) // 2

                all_same = same_pref[r] - same_pref[l] == 0
                if all_same:
                    out.append("0")
                    continue

                alternating = True
                if m >= 3:
                    alternating = alt_pref[r - 1] - alt_pref[l] == 0

                if alternating:
                    p = m // 2
                    out.append(str(p * (p + 1)))
                elif is_pal(l, r, d1, d2):
                    out.append(str(total - 1 - m))
                else:
                    out.append(str(total - 1))

        sys.stdout.write("\n".join(out))

    if __name__ == "__main__":
        solve()

# CLAUSE: finish_program
if __name__ == "__main__":
    _run_case_program()
