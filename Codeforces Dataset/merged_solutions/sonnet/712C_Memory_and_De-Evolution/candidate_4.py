import sys


# --- clause: read_input :: () -> tuple[int, int] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    pair = list(map(int, data[:2]))
    return pair[0], pair[1]


# --- clause: grow_steps :: (x: int, y: int) -> int ---
def grow_steps(x, y):
    sides = [y, y, y]
    steps = 0
    while True:
        smallest = 0
        for i in range(1, 3):
            if sides[i] < sides[smallest]:
                smallest = i
        if sides[smallest] >= x:
            return steps
        other = 0
        for i in range(3):
            if i != smallest:
                other += sides[i]
        grown = other - 1
        if grown > x:
            grown = x
        sides[smallest] = grown
        steps += 1


# --- clause: main :: () -> None ---
def main():
    x, y = read_input()
    answer = grow_steps(x, y)
    sys.stdout.write(str(answer) + "\n")


if __name__ == "__main__":
    main()
