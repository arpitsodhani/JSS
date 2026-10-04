import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    return numbers[1:1 + numbers[0]]


# --- clause: best_lucky :: (s: list[int]) -> int ---
def best_lucky(s):
    n = len(s)
    best = 0
    stack = []
    for i in range(n):
        value = s[i]
        while stack and stack[-1] < value:
            best = max(best, stack.pop() ^ value)
        if stack:
            best = max(best, stack[-1] ^ value)
        stack.append(value)
    return best


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write("%d\n" % best_lucky(read_input()))


if __name__ == "__main__":
    main()
