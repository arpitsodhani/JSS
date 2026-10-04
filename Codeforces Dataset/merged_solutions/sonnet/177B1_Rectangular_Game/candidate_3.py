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
        if current % 2 == 0:
            current //= 2
            continue
        divisor = current
        step = 3
        while step * step <= current:
            if current % step == 0:
                divisor = step
                break
            step += 2
        current //= divisor
    return total + 1


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write(str(game_total(read_input())) + "\n")


if __name__ == "__main__":
    main()
