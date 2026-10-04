import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    tokens = list(map(int, sys.stdin.buffer.read().split()))
    return tokens[1:1 + tokens[0]]


# --- clause: best_lucky :: (s: list[int]) -> int ---
def best_lucky(s):
    stack = []
    best = 0
    for item in s:
        while stack:
            here = stack[-1] ^ item
            if here > best:
                best = here
            if stack[-1] < item:
                stack.pop()
            else:
                break
        stack.append(item)
    return best


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write("%d\n" % best_lucky(read_input()))


if __name__ == "__main__":
    main()
