import sys


# --- clause: read_input :: () -> str ---
def read_input():
    return sys.stdin.buffer.read().split()[0].decode()


# --- clause: complexity :: (bits: str) -> int ---
def complexity(bits):
    mod = 1000000007
    element = int(bits, 2) % mod
    return element * pow(2, len(bits) - 1, mod) % mod


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write("%d\n" % complexity(read_input()))


if __name__ == "__main__":
    main()
