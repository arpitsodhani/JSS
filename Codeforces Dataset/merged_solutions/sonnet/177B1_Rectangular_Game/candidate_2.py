import sys


# --- clause: read_input :: () -> int ---
def read_input():
    return int(sys.stdin.buffer.read().split()[0])


# --- clause: game_total :: (n: int) -> int ---
def game_total(n):
    total = 1
    current = n
    while current > 1:
        total += current
        smallest = current
        step = 2
        while step * step <= current:
            if current % step == 0:
                smallest = step
                break
            step += 1
        current = current // smallest
    return total


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write(str(game_total(read_input())) + "\n")


if __name__ == "__main__":
    main()
