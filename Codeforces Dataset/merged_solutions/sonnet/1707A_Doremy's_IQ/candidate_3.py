import sys


# --- clause: read_input :: () -> list[tuple[int, list[int]]] ---
def read_input():
    fields = list(map(int, sys.stdin.buffer.read().split()))
    t = fields[0]
    cursor = 1
    cases = []
    for _ in range(t):
        n = fields[cursor]
        q = fields[cursor + 1]
        cursor += 2
        cases.append((q, fields[cursor:cursor + n]))
        cursor += n
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
    collected = []
    for q, a in read_input():
        collected.append(choose_contests(q, a))
    sys.stdout.write("\n".join(collected) + "\n")


if __name__ == "__main__":
    main()
