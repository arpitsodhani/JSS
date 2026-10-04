import sys


# --- clause: read_input :: () -> tuple[int, int] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    return numbers[0], numbers[1]


# --- clause: start_shell :: (n: int, x: int) -> int ---
def start_shell(n, x):
    place = x
    steps = n % 6
    while steps > 0:
        if steps % 2 == 1:
            if place == 0:
                place = 1
            elif place == 1:
                place = 0
        else:
            if place == 1:
                place = 2
            elif place == 2:
                place = 1
        steps -= 1
    return place


# --- clause: main :: () -> None ---
def main():
    n, x = read_input()
    sys.stdout.write("%d\n" % start_shell(n, x))


if __name__ == "__main__":
    main()
