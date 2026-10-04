import sys


# --- clause: read_input :: () -> str ---
def read_input():
    return sys.stdin.buffer.read().split()[0].decode()


# --- clause: complexity :: (bits: str) -> int ---
def complexity(bits):
    mod = 1000000007
    value = 0
    for ch in bits:
        value = (value * 2 + (1 if ch == "1" else 0)) % mod
    shift = 1
    for _ in range(len(bits) - 1):
        shift = shift * 2 % mod
    return value * shift % mod


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write("%d\n" % complexity(read_input()))


if __name__ == "__main__":
    main()
