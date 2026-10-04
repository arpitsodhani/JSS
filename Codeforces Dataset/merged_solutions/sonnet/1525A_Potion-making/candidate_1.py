import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    return data[1:1 + data[0]]


# --- clause: gcd_of :: (a: int, b: int) -> int ---
def gcd_of(a, b):
    while b:
        a, b = b, a % b
    return a


# --- clause: fewest_steps :: (k: int) -> int ---
def fewest_steps(k):
    return 100 // gcd_of(k, 100)


# --- clause: main :: () -> None ---
def main():
    out = []
    for k in read_input():
        out.append(fewest_steps(k))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
