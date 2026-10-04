import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    return numbers[1:1 + numbers[0]]


# --- clause: destroy_steps :: (h: list[int]) -> int ---
def destroy_steps(h):
    n = len(h)
    layers = [0] * n
    for i in range(n):
        edge = i + 1
        if n - i < edge:
            edge = n - i
        layers[i] = edge if edge < h[i] else h[i]
    for i in range(1, n):
        if layers[i] > layers[i - 1] + 1:
            layers[i] = layers[i - 1] + 1
    for i in range(n - 2, -1, -1):
        if layers[i] > layers[i + 1] + 1:
            layers[i] = layers[i + 1] + 1
    best = 0
    for value in layers:
        if value > best:
            best = value
    return best


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write("%d\n" % destroy_steps(read_input()))


if __name__ == "__main__":
    main()
