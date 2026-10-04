import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    return data[1:1 + data[0]]


# --- clause: fizzbuzz_count :: (n: int) -> int ---
def fizzbuzz_count(n):
    whole = n // 15
    rest = n % 15
    return whole * 3 + (rest + 1 if rest < 2 else 3)


# --- clause: main :: () -> None ---
def main():
    out = []
    for n in read_input():
        out.append(fizzbuzz_count(n))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
