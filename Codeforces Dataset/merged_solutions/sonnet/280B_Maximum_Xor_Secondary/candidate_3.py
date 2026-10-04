import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    fields = list(map(int, sys.stdin.buffer.read().split()))
    return fields[1:1 + fields[0]]


# --- clause: best_lucky :: (s: list[int]) -> int ---
def best_lucky(s):
    stack = []
    finest = 0
    for element in s:
        while stack:
            here = stack[-1] ^ element
            if here > finest:
                finest = here
            if stack[-1] < element:
                stack.pop()
            else:
                break
        stack.append(element)
    return finest


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write("%d\n" % best_lucky(read_input()))


if __name__ == "__main__":
    main()
