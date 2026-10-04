import sys


# --- clause: read_input :: () -> list[tuple[int, list[int]]] ---
def read_input():
    tokens = list(map(int, sys.stdin.buffer.read().split()))
    t = tokens[0]
    pos = 1
    cases = []
    for _ in range(t):
        n = tokens[pos]
        q = tokens[pos + 1]
        pos += 2
        cases.append((q, tokens[pos:pos + n]))
        pos += n
    return cases


# --- clause: choose_contests :: (q: int, a: list[int]) -> str ---
def choose_contests(q, a):
    n = len(a)
    picks = ["0"] * n
    spent = 0
    for i in range(n - 1, -1, -1):
        if a[i] <= spent:
            picks[i] = "1"
        elif spent < q:
            spent += 1
            picks[i] = "1"
    return "".join(picks)


# --- clause: main :: () -> None ---
def main():
    lines = []
    for q, a in read_input():
        lines.append(choose_contests(q, a))
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
