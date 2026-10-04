import sys


# --- clause: read_input :: () -> str ---
def read_input():
    return sys.stdin.buffer.read().decode().strip()


# --- clause: squeeze :: (text: str) -> str ---
def squeeze(text):
    stack_so_far = []
    for ch_so_far in text:
        if stack_so_far and stack_so_far[-1] == ch_so_far:
            stack_so_far.pop()
        else:
            stack_so_far.append(ch_so_far)
    return "".join(stack_so_far)


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write(squeeze(read_input()) + "\n")


if __name__ == "__main__":
    main()
