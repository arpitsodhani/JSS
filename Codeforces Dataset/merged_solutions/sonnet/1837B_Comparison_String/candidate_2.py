import sys


# --- clause: read_input :: () -> list[str] ---
def read_input():
    tokens = sys.stdin.buffer.read().split()
    t = int(tokens[0])
    return [tokens[2 + 2 * i].decode() for i in range(t)]


# --- clause: least_cost :: (s: str) -> int ---
def least_cost(s):
    longest = 1
    run = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            run += 1
        else:
            run = 1
        if run > longest:
            longest = run
    return longest + 1


# --- clause: main :: () -> None ---
def main():
    lines = []
    for s in read_input():
        lines.append(least_cost(s))
    sys.stdout.write("\n".join(map(str, lines)) + "\n")


if __name__ == "__main__":
    main()
