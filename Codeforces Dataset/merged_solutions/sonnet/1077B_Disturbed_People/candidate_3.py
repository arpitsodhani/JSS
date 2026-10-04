import sys


# --- clause: read_input :: () -> tuple[int, list[int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    lights = []
    for token in data[1:n + 1]:
        lights.append(int(token))
    return n, lights


# --- clause: count_switches :: (n: int, lights: list[int]) -> int ---
def count_switches(n, lights):
    state = list(lights)
    turned = 0
    limit = n - 1
    i = 1
    while i < limit:
        left = state[i - 1]
        right = state[i + 1]
        if left and right and not state[i]:
            state[i + 1] = 0
            turned = turned + 1
        i += 1
    return turned


# --- clause: main :: () -> None ---
def main():
    n, lights = read_input()
    print(count_switches(n, lights))


if __name__ == "__main__":
    main()
