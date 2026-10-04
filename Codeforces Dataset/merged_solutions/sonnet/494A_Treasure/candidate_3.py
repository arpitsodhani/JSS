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
    occurrences = []
    begin = hashes
    for ch in s:
        if ch == "#":
            begin -= 1
            occurrences.append(last if begin == 0 else 1)
    balance = 0
    at = 0
    for ch in s:
        if ch == "(":
            balance += 1
        elif ch == ")":
            balance -= 1
        else:
            balance -= occurrences[at]
            at += 1
        if balance < 0:
            return None
    if balance:
        return None
    return occurrences


# --- clause: main :: () -> None ---
def main():
    occurrences = share_closers(read_input())
    if occurrences is None:
        sys.stdout.write("-1\n")
    else:
        sys.stdout.write("\n".join(map(str, occurrences)) + "\n")


if __name__ == "__main__":
    main()
