# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys

    data = list(map(int, sys.stdin.read().split()))
    t = data[0]
    idx = 1
    ans = []

    for _ in range(t):
        n = data[idx]
        idx += 1
        year = 0
        for a in data[idx:idx + n]:
            year = (year // a + 1) * a
        idx += n
        ans.append(str(year))

    print("\n".join(ans))

# CLAUSE: finish_program
def main():
    _inner_main()

main()
