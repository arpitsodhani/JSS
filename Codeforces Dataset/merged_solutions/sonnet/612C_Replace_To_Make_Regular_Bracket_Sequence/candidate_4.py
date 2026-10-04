import sys


# --- clause: read_input :: () -> str ---
def read_input():
    return sys.stdin.buffer.read().split()[0].decode()


# --- clause: fewest_replaces :: (s: str) -> int ---
def fewest_replaces(s):
    opens = "([{<"
    closes = ")]}>"
    stack = []
    changes = 0
    for ch in s:
        spot = closes.find(ch)
        if spot < 0:
            stack.append(opens.find(ch))
            continue
        if not stack:
            return -1
        if stack.pop() != spot:
            changes += 1
    return -1 if stack else changes


# --- clause: main :: () -> None ---
def main():
    outcome = fewest_replaces(read_input())
    sys.stdout.write("Impossible\n" if outcome < 0 else "%d\n" % outcome)


if __name__ == "__main__":
    main()
