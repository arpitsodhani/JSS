import sys


# --- clause: read_input :: () -> str ---
def read_input():
    return sys.stdin.buffer.read().split()[0].decode()


# --- clause: longest_zebra :: (s: str) -> int ---
def longest_zebra(s):
    n = len(s)
    doubled = s + s
    best = 1
    run = 1
    for i in range(1, len(doubled)):
        if doubled[i] != doubled[i - 1]:
            run += 1
        else:
            run = 1
        if run > best:
            best = run
    return best if best < n else n


# --- clause: main :: () -> None ---
def main():
    s = read_input()
    sys.stdout.write(str(longest_zebra(s)) + "\n")


if __name__ == "__main__":
    main()
