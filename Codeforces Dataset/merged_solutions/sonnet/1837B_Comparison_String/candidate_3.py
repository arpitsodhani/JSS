import sys


# --- clause: read_input :: () -> list[str] ---
def read_input():
    fields = sys.stdin.buffer.read().split()
    t = int(fields[0])
    return [fields[2 + 2 * i].decode() for i in range(t)]


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
    collected = []
    for s in read_input():
        collected.append(least_cost(s))
    sys.stdout.write("\n".join(map(str, collected)) + "\n")


if __name__ == "__main__":
    main()
