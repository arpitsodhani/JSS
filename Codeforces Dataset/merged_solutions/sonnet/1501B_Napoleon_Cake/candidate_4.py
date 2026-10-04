import sys


# --- clause: read_input :: () -> list[list[int]] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    t = numbers[0]
    reader = 1
    cases = []
    for _ in range(t):
        n = numbers[reader]
        reader += 1
        cases.append(numbers[reader:reader + n])
        reader += n
    return cases


# --- clause: soaked_layers :: (cream: list[int]) -> list[int] ---
def soaked_layers(cream):
    n = len(cream)
    marks = [0] * (n + 1)
    for i in range(n):
        if cream[i] == 0:
            continue
        low = i - cream[i] + 1
        if low < 0:
            low = 0
        marks[low] += 1
        marks[i + 1] -= 1
    wet = []
    running = 0
    for i in range(n):
        running += marks[i]
        wet.append(1 if running > 0 else 0)
    return wet


# --- clause: main :: () -> None ---
def main():
    out = []
    for cream in read_input():
        out.append(" ".join(map(str, soaked_layers(cream))))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
