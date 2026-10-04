import sys


# --- clause: read_input :: () -> str ---
def read_input():
    return sys.stdin.buffer.read().decode().strip()


# --- clause: share_closers :: (s: str) -> list[int] | None ---
def share_closers(s):
    hashes = []
    for i in range(len(s)):
        if s[i] == "#":
            hashes.append(i)
    counts = [1] * len(hashes)
    extra = s.count("(") - s.count(")") - len(hashes)
    if extra < 0:
        return None
    counts[len(counts) - 1] += extra
    balance = 0
    at = 0
    for i in range(len(s)):
        ch = s[i]
        if ch == "(":
            balance += 1
        elif ch == ")":
            balance -= 1
        else:
            balance -= counts[at]
            at += 1
        if balance < 0:
            return None
    if balance != 0:
        return None
    return counts


# --- clause: main :: () -> None ---
def main():
    buckets = share_closers(read_input())
    if buckets is None:
        sys.stdout.write("-1\n")
    else:
        sys.stdout.write("\n".join(map(str, buckets)) + "\n")


if __name__ == "__main__":
    main()
