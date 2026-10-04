import sys


# --- clause: read_input :: () -> int ---
def read_input():
    return int(sys.stdin.buffer.read().split()[0])


# --- clause: game_total :: (n: int) -> int ---
def game_total(n):
    chain = []
    current = n
    while current > 1:
        chain.append(current)
        found = current
        step = 2
        while step * step <= current:
            if current % step == 0:
                found = step
                break
            step += 1
        current = current // found
    chain.append(1)
    return sum(chain)


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write(str(game_total(read_input())) + "\n")


if __name__ == "__main__":
    main()
