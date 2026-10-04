import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    return data[1:1 + data[0]]


# --- clause: build_string :: (n: int) -> str ---
def build_string(n):
    if n == 1:
        return "a"
    letters = []
    extra = n % 2
    half = (n - extra) // 2
    letters.append("a" * half)
    letters.append("b")
    letters.append("a" * (half - 1))
    if extra:
        letters.append("c")
    return "".join(letters)


# --- clause: main :: () -> None ---
def main():
    out = []
    for n in read_input():
        out.append(build_string(n))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
