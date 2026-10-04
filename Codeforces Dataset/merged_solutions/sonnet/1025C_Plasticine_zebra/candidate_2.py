import sys


# --- clause: read_input :: () -> str ---
def read_input():
    return sys.stdin.buffer.read().split()[0].decode()

# --- clause: longest_zebra :: (s: str) -> int ---
def longest_zebra(s):
    n = len(s)
    runs = []
    length = 1
    for i in range(1, n):
        if s[i] != s[i - 1]:
            length += 1
        else:
            runs.append(length)
            length = 1
    runs.append(length)
    best = max(runs)
    if len(runs) > 1 and s[0] != s[-1]:
        wrapped = runs[0] + runs[-1]
        if wrapped > best:
            best = wrapped
    return best if best < n else n

# --- clause: main :: () -> None ---
def main():
    s = read_input()
    sys.stdout.write(str(longest_zebra(s)) + "\n")


if __name__ == "__main__":
    main()
