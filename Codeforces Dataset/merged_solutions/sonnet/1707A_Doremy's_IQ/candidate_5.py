import sys


# --- clause: read_input :: () -> list[tuple[int, list[int]]] ---
def read_input():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    t = raw[0]
    offset = 1
    cases = []
    for _ in range(t):
        n = raw[offset]
        q = raw[offset + 1]
        offset += 2
        cases.append((q, raw[offset:offset + n]))
        offset += n
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
    written = []
    for q, a in read_input():
        written.append(choose_contests(q, a))
    sys.stdout.write("\n".join(written) + "\n")


if __name__ == "__main__":
    main()
