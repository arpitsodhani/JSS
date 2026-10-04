import sys


# --- clause: read_input :: () -> int ---
def read_input():
    return int(sys.stdin.buffer.read().split()[0])


# --- clause: fibonacci_upto :: (n: int) -> set[int] ---
def fibonacci_upto(n):
    marks = set()
    previous = 1
    current = 1
    while previous <= n:
        marks.add(previous)
        previous, current = current, previous + current
    return marks


# --- clause: build_name :: (n: int, marks: set[int]) -> str ---
def build_name(n, marks):
    letters = []
    for i in range(1, n + 1):
        letters.append("O" if i in marks else "o")
    return "".join(letters)


# --- clause: main :: () -> None ---
def main():
    n = read_input()
    sys.stdout.write(build_name(n, fibonacci_upto(n)) + "\n")


if __name__ == "__main__":
    main()
