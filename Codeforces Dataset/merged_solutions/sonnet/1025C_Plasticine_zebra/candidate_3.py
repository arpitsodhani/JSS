import sys


# --- clause: read_input :: () -> str ---
def read_input():
    return sys.stdin.buffer.read().split()[0].decode()

# --- clause: longest_zebra :: (s: str) -> int ---
def longest_zebra(s):
    n = len(s)
    twice = s * 2
    best = 1
    start = 0
    for i in range(1, len(twice)):
        if twice[i] == twice[i - 1]:
            start = i
        elif i - start + 1 > best:
            best = i - start + 1
    return n if best > n else best

# --- clause: main :: () -> None ---
def main():
    s = read_input()
    sys.stdout.write(str(longest_zebra(s)) + "\n")


if __name__ == "__main__":
    main()
