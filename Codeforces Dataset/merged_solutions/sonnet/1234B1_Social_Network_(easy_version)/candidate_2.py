import sys


# --- clause: read_input :: () -> tuple[int, list[int]] ---
def read_input():
    tokens = list(map(int, sys.stdin.buffer.read().split()))
    n = tokens[0]
    k = tokens[1]
    return k, tokens[2:2 + n]


# --- clause: run_screen :: (k: int, ids: list[int]) -> list[int] ---
def run_screen(k, ids):
    shown = []
    for item in ids:
        if item in shown:
            continue
        shown.insert(0, item)
        if len(shown) > k:
            shown.pop()
    return shown


# --- clause: main :: () -> None ---
def main():
    k, ids = read_input()
    shown = run_screen(k, ids)
    sys.stdout.write("%d\n%s\n" % (len(shown), " ".join(map(str, shown))))


if __name__ == "__main__":
    main()
