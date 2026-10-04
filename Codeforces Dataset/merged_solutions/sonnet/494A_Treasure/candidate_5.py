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
    frequency = []
    first_side = hashes
    for ch in s:
        if ch == "#":
            first_side -= 1
            frequency.append(last if first_side == 0 else 1)
    balance = 0
    at = 0
    for ch in s:
        if ch == "(":
            balance += 1
        elif ch == ")":
            balance -= 1
        else:
            balance -= frequency[at]
            at += 1
        if balance < 0:
            return None
    if balance:
        return None
    return frequency


# --- clause: main :: () -> None ---
def main():
    frequency = share_closers(read_input())
    if frequency is None:
        sys.stdout.write("-1\n")
    else:
        sys.stdout.write("\n".join(map(str, frequency)) + "\n")


if __name__ == "__main__":
    main()
