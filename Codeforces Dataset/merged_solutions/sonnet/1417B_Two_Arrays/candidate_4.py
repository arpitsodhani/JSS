import sys


# --- clause: read_input :: () -> list[tuple[int, list[int]]] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    t = numbers[0]
    cursor = 1
    cases = []
    for _ in range(t):
        n = numbers[cursor]
        target = numbers[cursor + 1]
        cursor += 2
        cases.append((target, numbers[cursor:cursor + n]))
        cursor += n
    return cases


# --- clause: paint :: (target: int, a: list[int]) -> list[int] ---
def paint(target, a):
    colours = [0] * len(a)
    middles = []
    for i in range(len(a)):
        twice = 2 * a[i]
        if twice > target:
            colours[i] = 1
        elif twice == target:
            middles.append(i)
    for spot in range(len(middles)):
        colours[middles[spot]] = spot % 2
    return colours


# --- clause: main :: () -> None ---
def main():
    out = []
    for target, a in read_input():
        out.append(" ".join(map(str, paint(target, a))))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
