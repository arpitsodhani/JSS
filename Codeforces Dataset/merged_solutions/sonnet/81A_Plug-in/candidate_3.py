import sys


# --- clause: read_input :: () -> str ---
def read_input():
    return sys.stdin.buffer.read().decode().strip()


# --- clause: squeeze :: (text: str) -> str ---
def squeeze(text):
    stack_value = []
    for ch_value in text:
        if stack_value and stack_value[-1] == ch_value:
            stack_value.pop()
        else:
            stack_value.append(ch_value)
    return "".join(stack_value)


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write(squeeze(read_input()) + "\n")


if __name__ == "__main__":
    main()
