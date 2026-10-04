import sys


# --- clause: read_input :: () -> int ---
def read_input():
    return int(sys.stdin.buffer.read().split()[0])


# --- clause: game_total :: (n: int) -> int ---
def game_total(n):
    total = 0
    current = n
    while current > 1:
        total += current
        factor = 0
        step = 2
        while step * step <= current:
            if current % step == 0:
                factor = step
                break
            step += 1
        if factor == 0:
            factor = current
        current //= factor
    return total + 1


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write(str(game_total(read_input())) + "\n")


if __name__ == "__main__":
    main()
