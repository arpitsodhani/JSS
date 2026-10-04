import sys


# --- clause: read_input :: () -> list[str] ---
def read_input():
    tokens = sys.stdin.buffer.read().split()
    t = int(tokens[0])
    cases = []
    for i in range(t):
        cases.append(tokens[2 + 2 * i].decode())
    return cases


# --- clause: build_matrix :: (s: str) -> list[str] | None ---
def build_matrix(s):
    n = len(s)
    winners = [i for i in range(n) if s[i] == "2"]
    if 0 < len(winners) < 3:
        return None
    grid = [["="] * n for _ in range(n)]
    for i in range(n):
        grid[i][i] = "X"
    for i in range(len(winners)):
        me = winners[i]
        prey = winners[(i + 1) % len(winners)]
        grid[me][prey] = "+"
        grid[prey][me] = "-"
    return ["".join(line) for line in grid]


# --- clause: main :: () -> None ---
def main():
    out = []
    for s in read_input():
        grid = build_matrix(s)
        if grid is None:
            out.append("NO")
        else:
            out.append("YES")
            out.extend(grid)
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
