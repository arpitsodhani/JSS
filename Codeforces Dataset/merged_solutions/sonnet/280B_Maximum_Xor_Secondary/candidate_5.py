import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    return raw[1:1 + raw[0]]


# --- clause: best_lucky :: (s: list[int]) -> int ---
def best_lucky(s):
    stack = []
    top = 0
    for number in s:
        while stack:
            here = stack[-1] ^ number
            if here > top:
                top = here
            if stack[-1] < number:
                stack.pop()
            else:
                break
        stack.append(number)
    return top


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write("%d\n" % best_lucky(read_input()))


if __name__ == "__main__":
    main()
