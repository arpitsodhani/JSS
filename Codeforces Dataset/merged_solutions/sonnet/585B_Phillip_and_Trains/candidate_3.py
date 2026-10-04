# CLAUSE: setup_environment
import sys

def main():
    tokens = sys.stdin.read().split()
    at = 0
    tests = int(tokens[at])
    at += 1
    answers = []

# CLAUSE: solve_logic
    for _ in range(tests):
        n = int(tokens[at])
        at += 2
        rows = []
        active = set()
        for r in range(3):
            s = tokens[at]
            at += 1
            for c, ch in enumerate(s):
                if ch == "s":
                    active.add((r, c))
            rows.append(s.replace("s", ".") + "." * 18)

        possible = False
        for time in range(n + 5):
            nxt = set()
            for r, c in active:
                shifted = c + 2 * time
                if shifted < n and rows[r][shifted] != ".":
                    continue
                if c >= n - 1:
                    possible = True
                    break
                nc = c + 1
                for nr in range(max(0, r - 1), min(3, r + 2)):
                    before = nc + 2 * time
                    after = nc + 2 * (time + 1)
                    if before < n and rows[nr][before] != ".":
                        continue
                    if after < n and rows[nr][after] != ".":
                        continue
                    nxt.add((nr, nc))
            if possible:
                break
            active = nxt
            if not active:
                break

        answers.append("YES" if possible else "NO")

# CLAUSE: finish_program
    print("\n".join(answers))

if __name__ == "__main__":
    main()
