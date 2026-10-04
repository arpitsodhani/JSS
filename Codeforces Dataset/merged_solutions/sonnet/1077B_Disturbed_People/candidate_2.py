import sys


# --- clause: read_input :: () -> tuple[int, list[int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    lights = list(map(int, data[1:n + 1]))
    return n, lights


# --- clause: count_switches :: (n: int, lights: list[int]) -> int ---
def count_switches(n, lights):
    state = list(lights)
    turned = 0
    for i in range(1, n - 1):
        if state[i - 1] == 1 and state[i] == 0 and state[i + 1] == 1:
            state[i + 1] = 0
            turned += 1
    return turned


# --- clause: main :: () -> None ---
def main():
    n, lights = read_input()
    sys.stdout.write("%d\n" % count_switches(n, lights))


if __name__ == "__main__":
    main()
