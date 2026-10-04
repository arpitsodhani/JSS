import sys


# --- clause: read_input :: () -> str ---
def read_input():
    return sys.stdin.buffer.read().decode().strip()


# --- clause: share_closers :: (s: str) -> list[int] | None ---
def share_closers(s):
    opens = s.count("(")
    closes = s.count(")")
    hashes = s.count("#")
    last = opens - closes - (hashes - 1)
    if last < 1:
        return None
    counts = []
    left = hashes
    for ch in s:
        if ch == "#":
            left -= 1
            counts.append(last if left == 0 else 1)
    balance = 0
    at = 0
    for ch in s:
        if ch == "(":
            balance += 1
        elif ch == ")":
            balance -= 1
        else:
            balance -= counts[at]
            at += 1
        if balance < 0:
            return None
    if balance:
        return None
    return counts


# --- clause: main :: () -> None ---
def main():
    counts = share_closers(read_input())
    if counts is None:
        sys.stdout.write("-1\n")
    else:
        sys.stdout.write("\n".join(map(str, counts)) + "\n")


if __name__ == "__main__":
    main()
