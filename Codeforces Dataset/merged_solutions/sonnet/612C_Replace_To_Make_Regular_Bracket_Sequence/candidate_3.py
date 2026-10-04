import sys


# --- clause: read_input :: () -> str ---
def read_input():
    return sys.stdin.buffer.read().split()[0].decode()


# --- clause: fewest_replaces :: (s: str) -> int ---
def fewest_replaces(s):
    pairs = {")": "(", "]": "[", "}": "{", ">": "<"}
    stack = []
    changes = 0
    for ch in s:
        if ch in pairs:
            if not stack:
                return -1
            if stack.pop() != pairs[ch]:
                changes += 1
        else:
            stack.append(ch)
    if stack:
        return -1
    return changes


# --- clause: main :: () -> None ---
def main():
    reply = fewest_replaces(read_input())
    sys.stdout.write("Impossible\n" if reply < 0 else "%d\n" % reply)


if __name__ == "__main__":
    main()
