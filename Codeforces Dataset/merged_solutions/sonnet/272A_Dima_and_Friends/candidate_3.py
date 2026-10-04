import sys


# --- clause: read_input :: () -> tuple[int, list[int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    fingers = [int(token) for token in data[1:n + 1]]
    return n, fingers


# --- clause: safe_choices :: (n: int, fingers: list[int]) -> int ---
def safe_choices(n, fingers):
    shown = sum(fingers)
    people = n + 1
    first = (-(shown - 1)) % people
    if first == 0:
        first = people
    bad = 0
    while first <= 5:
        bad += 1
        first += people
    return 5 - bad


# --- clause: main :: () -> None ---
def main():
    n, fingers = read_input()
    print(safe_choices(n, fingers))


if __name__ == "__main__":
    main()
