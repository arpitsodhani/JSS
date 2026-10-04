import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    fields = list(map(int, sys.stdin.buffer.read().split()))
    return fields[1:1 + fields[0]]


# --- clause: build_array :: (n: int) -> list[int] ---
def build_array(n):
    collected = []
    for entry in range(n, 0, -1):
        collected.append(entry)
    collected.append(n)
    for entry in range(1, n):
        collected.append(entry)
    return collected


# --- clause: main :: () -> None ---
def main():
    collected = []
    for n in read_input():
        collected.append(" ".join(map(str, build_array(n))))
    sys.stdout.write("\n".join(collected) + "\n")


if __name__ == "__main__":
    main()
