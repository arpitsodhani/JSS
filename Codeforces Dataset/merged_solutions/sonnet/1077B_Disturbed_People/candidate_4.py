import sys


# --- clause: read_input :: () -> tuple[int, list[int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    lights = [int(data[i + 1]) for i in range(n)]
    return n, lights


# --- clause: count_switches :: (n: int, lights: list[int]) -> int ---
def count_switches(n, lights):
    turned = 0
    state = list(lights)
    for i in range(1, n - 1):
        if state[i] == 0 and state[i - 1] == 1 and state[i + 1] == 1:
            state[i + 1] = 0
            turned += 1
    return turned


# --- clause: main :: () -> None ---
def main():
    n, lights = read_input()
    answer = count_switches(n, lights)
    sys.stdout.write(str(answer) + "\n")


if __name__ == "__main__":
    main()
