# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys

    def solve_case(s):
        n = len(s)
        doubled = s + s
        cur = 0
        ans = 0
        for ch in doubled:
            if ch == '1':
                cur = 0
            else:
                cur += 1
                ans = max(ans, cur)
        return ans

    data = sys.stdin.read().strip().split()
    if not data:
        sys.exit()

    t = int(data[0])
    res = []
    idx = 1
    for _ in range(t):
        n = int(data[idx])
        s = data[idx + 1].strip()
        idx += 2
        res.append(str(solve_case(s)))

    print("\n".join(res))

# CLAUSE: finish_program
def main():
    _inner_main()

main()
