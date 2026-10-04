# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _run_case_program():
    import sys

    def solve_case(n, s, a):
        inf = 10**9
        ok = {0b0011, 0b0101}
        dp = {0: 0}

        for i in range(n):
            ndp = {}
            for mask, cost in dp.items():
                for b in (0, 1):
                    nmask = ((mask << 1) | b) & 15
                    if i >= 3 and a[i - 3] == '1' and nmask not in ok:
                        continue
                    add = (b != (1 if s[i] == ')' else 0))
                    key = nmask & 7
                    val = cost + add
                    if val < ndp.get(key, inf):
                        ndp[key] = val
            dp = ndp
            if not dp:
                return -1

        return min(dp.values()) if dp else -1

    def main():
        data = sys.stdin.read().strip().split()
        if not data:
            return

        t = int(data[0])
        idx = 1
        ans = []

        for _ in range(t):
            n = int(data[idx])
            idx += 1
            s = data[idx]
            idx += 1
            a = data[idx]
            idx += 1
            ans.append(str(solve_case(n, s, a)))

        print("\n".join(ans))

    if __name__ == "__main__":
        main()

# CLAUSE: finish_program
if __name__ == "__main__":
    _run_case_program()
