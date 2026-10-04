import sys


# --- clause: read_input :: () -> str ---
def read_input():
    return sys.stdin.buffer.read().decode().strip()


# --- clause: squeeze :: (text: str) -> str ---
def squeeze(text):
    stack_seen = []
    for ch_seen in text:
        if stack_seen and stack_seen[-1] == ch_seen:
            stack_seen.pop()
        else:
            stack_seen.append(ch_seen)
    return "".join(stack_seen)


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write(squeeze(read_input()) + "\n")


if __name__ == "__main__":
    main()
