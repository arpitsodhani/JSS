import sys


# --- clause: read_input :: () -> tuple[int, list[int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    fingers = [int(data[i + 1]) for i in range(n)]
    return n, fingers


# --- clause: safe_choices :: (n: int, fingers: list[int]) -> int ---
def safe_choices(n, fingers):
    shown = 0
    for value in fingers:
        shown += value
    people = n + 1
    good = 0
    for mine in range(1, 6):
        if (shown + mine - 1) % people:
            good += 1
    return good


# --- clause: main :: () -> None ---
def main():
    n, fingers = read_input()
    answer = safe_choices(n, fingers)
    sys.stdout.write(str(answer) + "\n")


if __name__ == "__main__":
    main()
