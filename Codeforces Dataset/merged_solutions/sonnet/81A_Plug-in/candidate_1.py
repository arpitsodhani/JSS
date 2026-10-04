import sys


# --- clause: read_input :: () -> str ---
def read_input():
    return sys.stdin.buffer.read().decode().strip()


# --- clause: squeeze :: (text: str) -> str ---
def squeeze(text):
    stack = []
    for ch in text:
        if stack and stack[-1] == ch:
            stack.pop()
        else:
            stack.append(ch)
    return "".join(stack)


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write(squeeze(read_input()) + "\n")


if __name__ == "__main__":
    main()
