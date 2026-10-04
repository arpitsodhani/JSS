import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    return data[1:1 + data[0]]


# --- clause: minutes_needed :: (n: int) -> int ---
def minutes_needed(n):
    if n <= 3:
        return 2 if n == 1 else 1
    return -(-n // 3)


# --- clause: main :: () -> None ---
def main():
    out = []
    for n in read_input():
        out.append(str(minutes_needed(n)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
