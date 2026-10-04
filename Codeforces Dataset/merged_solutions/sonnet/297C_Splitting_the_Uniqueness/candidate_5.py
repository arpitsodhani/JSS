# CLAUSE: setup_environment
from sys import stdin, stdout

# CLAUSE: solve_logic
def main():
    raw = stdin.buffer.read().split()
    if len(raw) == 0:
        return

    n = int(raw[0])
    s = list(map(int, raw[1:1 + n]))
    positions = sorted(range(n), key=lambda pos: (s[pos], pos))

    a = [None] * n
    b = [None] * n
    seen = set()
    ok = True

    for rank, pos in zip(range(n), positions):
        value = s[pos] - rank
        if value < 0:
            ok = False
            break
        if value in seen:
            ok = False
            break
        seen.add(value)
        a[pos] = rank
        b[pos] = value

    if not ok:
        stdout.write("NO\n")
    else:
        stdout.write("YES\n")
        stdout.write(" ".join(map(str, a)) + "\n")
        stdout.write(" ".join(map(str, b)) + "\n")

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
