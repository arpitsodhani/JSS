import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    fields = list(map(int, sys.stdin.buffer.read().split()))
    return fields[1:1 + fields[0]]


# --- clause: hardness_steps :: (order: list[int]) -> list[int] ---
def hardness_steps(order):
    n = len(order)
    placed = [False] * (n + 2)
    tail = n
    collected = [1]
    for i in range(n):
        placed[order[i]] = True
        while tail >= 1 and placed[tail]:
            tail -= 1
        collected.append(i + 1 - (n - tail) + 1)
    return collected


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write(" ".join(map(str, hardness_steps(read_input()))) + "\n")


if __name__ == "__main__":
    main()
