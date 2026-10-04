import sys


# --- clause: read_input :: () -> str ---
def read_input():
    return sys.stdin.buffer.read().split()[0].decode()

# --- clause: longest_zebra :: (s: str) -> int ---
def longest_zebra(s):
    n = len(s)
    blocks = []
    current = 1
    for previous, letter in zip(s, s[1:]):
        if letter == previous:
            blocks.append(current)
            current = 1
        else:
            current += 1
    blocks.append(current)
    best = 0
    for value in blocks:
        if value > best:
            best = value
    if len(blocks) > 1 and s[0] != s[-1] and blocks[0] + blocks[-1] > best:
        best = blocks[0] + blocks[-1]
    return n if best > n else best

# --- clause: main :: () -> None ---
def main():
    s = read_input()
    sys.stdout.write(str(longest_zebra(s)) + "\n")


if __name__ == "__main__":
    main()
