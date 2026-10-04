import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    return numbers[1:1 + numbers[0]]


# --- clause: hardness_steps :: (order: list[int]) -> list[int] ---
def hardness_steps(order):
    n = len(order)
    placed = set()
    tail = n
    out = [1]
    done = 0
    for i in range(n):
        placed.add(order[i])
        while tail in placed:
            placed.discard(tail)
            tail -= 1
            done += 1
        out.append(i + 2 - done)
    return out


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write(" ".join(map(str, hardness_steps(read_input()))) + "\n")


if __name__ == "__main__":
    main()
