import sys


# --- clause: read_input :: () -> list[tuple[int, list[int]]] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    t = numbers[0]
    reader = 1
    cases = []
    for _ in range(t):
        n = numbers[reader]
        q = numbers[reader + 1]
        reader += 2
        cases.append((q, numbers[reader:reader + n]))
        reader += n
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
    out = []
    for q, a in read_input():
        out.append(choose_contests(q, a))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
