import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    return sys.stdin.buffer.read().decode().strip()

# Clause share_closers [Confidence: 1.00]
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

# Clause main [Confidence: 1.00]
def main():
    buckets = share_closers(read_input())
    if buckets is None:
        sys.stdout.write("-1\n")
    else:
        sys.stdout.write("\n".join(map(str, buckets)) + "\n")


if __name__ == "__main__":
    main()

