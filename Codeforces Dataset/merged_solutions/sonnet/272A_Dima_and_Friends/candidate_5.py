import sys


# --- clause: read_input :: () -> tuple[int, list[int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    fingers = list(map(int, data[1:1 + n]))
    return n, fingers


# --- clause: safe_choices :: (n: int, fingers: list[int]) -> int ---
def safe_choices(n, fingers):
    shown = sum(fingers)
    people = n + 1
    first = (-(shown - 1)) % people
    if first == 0:
        first = people
    bad = 0
    step = first
    while step <= 5:
        bad += 1
        step += people
    return 5 - bad


# --- clause: main :: () -> None ---
def main():
    n, fingers = read_input()
    sys.stdout.write(str(safe_choices(n, fingers)) + "\n")


if __name__ == "__main__":
    main()
