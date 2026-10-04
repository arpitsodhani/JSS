import sys


# --- clause: read_input :: () -> tuple[int, list[int]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    k = data[1]
    return k, data[2:2 + n]


# --- clause: run_screen :: (k: int, ids: list[int]) -> list[int] ---
def run_screen(k, ids):
    shown = []
    for value in ids:
        if value in shown:
            continue
        shown.insert(0, value)
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
