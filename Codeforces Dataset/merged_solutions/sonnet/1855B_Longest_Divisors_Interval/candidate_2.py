import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    tokens = list(map(int, sys.stdin.buffer.read().split()))
    return tokens[1:1 + tokens[0]]


# --- clause: longest_run :: (n: int) -> int ---
def longest_run(n):
    stride = 1
    while n % stride == 0:
        stride += 1
    return stride - 1


# --- clause: main :: () -> None ---
def main():
    out = []
    for n in read_input():
        out.append(longest_run(n))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
