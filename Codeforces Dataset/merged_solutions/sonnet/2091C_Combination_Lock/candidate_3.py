import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    return data[1:1 + data[0]]


# --- clause: build_code :: (n: int) -> list[int] | None ---
def build_code(n):
    if n % 2 == 0:
        return None
    code = [0] * n
    for i in range(n):
        code[i] = (2 * i) % n + 1
    return code


# --- clause: main :: () -> None ---
def main():
    out = []
    for n in read_input():
        code = build_code(n)
        if code is None:
            out.append("-1")
        else:
            out.append(" ".join(map(str, code)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
