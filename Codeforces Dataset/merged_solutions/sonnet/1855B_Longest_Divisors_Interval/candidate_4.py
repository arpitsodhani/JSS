import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    return numbers[1:1 + numbers[0]]


# --- clause: longest_run :: (n: int) -> int ---
def longest_run(n):
    for step in range(1, 60):
        if n % step:
            return step - 1
    return 59


# --- clause: main :: () -> None ---
def main():
    out = []
    for n in read_input():
        out.append(longest_run(n))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
