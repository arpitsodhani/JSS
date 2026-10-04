import sys


# --- clause: read_input :: () -> str ---
def read_input():
    return sys.stdin.buffer.read().decode().strip()


# --- clause: squeeze :: (text: str) -> str ---
def squeeze(text):
    stack = []
    at = 0
    while at < len(text):
        ch = text[at]
        if len(stack) and stack[len(stack) - 1] == ch:
            del stack[len(stack) - 1]
        else:
            stack.append(ch)
        at += 1
    return "".join(stack)


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write(squeeze(read_input()) + "\n")


if __name__ == "__main__":
    main()
