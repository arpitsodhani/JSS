import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    return raw[1:1 + raw[0]]


# --- clause: fizzbuzz_count :: (n: int) -> int ---
def fizzbuzz_count(n):
    whole = n // 15
    rest = n % 15
    return whole * 3 + (rest + 1 if rest < 2 else 3)


# --- clause: main :: () -> None ---
def main():
    written = []
    for n in read_input():
        written.append(fizzbuzz_count(n))
    sys.stdout.write("\n".join(map(str, written)) + "\n")


if __name__ == "__main__":
    main()
