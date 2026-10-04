import sys


# --- clause: read_input :: () -> tuple[int, list[int]] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    n = numbers[0]
    k = numbers[1]
    return k, numbers[2:2 + n]


# --- clause: run_screen :: (k: int, ids: list[int]) -> list[int] ---
def run_screen(k, ids):
    shown = []
    on_screen = set()
    at = 0
    while at < len(ids):
        value = ids[at]
        at += 1
        if value in on_screen:
            continue
        shown.insert(0, value)
        on_screen.add(value)
        if len(shown) > k:
            on_screen.discard(shown.pop())
    return shown


# --- clause: main :: () -> None ---
def main():
    k, ids = read_input()
    shown = run_screen(k, ids)
    sys.stdout.write("%d\n%s\n" % (len(shown), " ".join(map(str, shown))))


if __name__ == "__main__":
    main()
