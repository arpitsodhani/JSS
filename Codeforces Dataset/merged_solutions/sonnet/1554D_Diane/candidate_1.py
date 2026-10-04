import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    return data[1:1 + data[0]]


# --- clause: build_string :: (n: int) -> str ---
def build_string(n):
    if n == 1:
        return "a"
    if n % 2 == 0:
        half = n // 2
        return "a" * half + "b" + "a" * (half - 1)
    head = (n - 1) // 2
    return "a" * head + "b" + "a" * (head - 1) + "c"


# --- clause: main :: () -> None ---
def main():
    out = []
    for n in read_input():
        out.append(build_string(n))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
