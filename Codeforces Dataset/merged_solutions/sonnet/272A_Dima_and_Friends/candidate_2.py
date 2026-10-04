import sys


# --- clause: read_input :: () -> tuple[int, list[int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    fingers = list(map(int, data[1:n + 1]))
    return n, fingers


# --- clause: safe_choices :: (n: int, fingers: list[int]) -> int ---
def safe_choices(n, fingers):
    shown = sum(fingers)
    people = n + 1
    good = 0
    for mine in range(1, 6):
        if (shown + mine - 1) % people:
            good += 1
    return good


# --- clause: main :: () -> None ---
def main():
    n, fingers = read_input()
    sys.stdout.write("%d\n" % safe_choices(n, fingers))


if __name__ == "__main__":
    main()
