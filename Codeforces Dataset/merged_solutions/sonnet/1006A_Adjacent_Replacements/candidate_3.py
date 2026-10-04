import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    fields = list(map(int, sys.stdin.buffer.read().split()))
    return fields[1:1 + fields[0]]


# --- clause: settle :: (a: list[int]) -> list[int] ---
def settle(a):
    collected = []
    for entry in a:
        collected.append(entry - 1 if entry % 2 == 0 else entry)
    return collected


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write(" ".join(map(str, settle(read_input()))) + "\n")


if __name__ == "__main__":
    main()
