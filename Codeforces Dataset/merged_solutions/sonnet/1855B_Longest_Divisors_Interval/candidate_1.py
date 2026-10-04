import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    return data[1:1 + data[0]]


# --- clause: longest_run :: (n: int) -> int ---
def longest_run(n):
    step = 1
    while n % step == 0:
        step += 1
    return step - 1


# --- clause: main :: () -> None ---
def main():
    out = []
    for n in read_input():
        out.append(longest_run(n))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
