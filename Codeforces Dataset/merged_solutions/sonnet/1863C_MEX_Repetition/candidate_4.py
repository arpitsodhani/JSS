import sys


# --- clause: read_input :: () -> list[tuple[int, list[int]]] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    t = numbers[0]
    reader = 1
    cases = []
    for _ in range(t):
        n = numbers[reader]
        k = numbers[reader + 1]
        reader += 2
        cases.append((k, numbers[reader:reader + n]))
        reader += n
    return cases


# --- clause: spin :: (k: int, a: list[int]) -> list[int] ---
def spin(k, a):
    n = len(a)
    total = (n + 1) * n // 2
    missing = total - sum(a)
    circle = list(a)
    circle.append(missing)
    shift = k % (n + 1)
    out = []
    for i in range(n):
        out.append(circle[(i - shift) % (n + 1)])
    return out


# --- clause: main :: () -> None ---
def main():
    out = []
    for k, a in read_input():
        out.append(" ".join(map(str, spin(k, a))))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
