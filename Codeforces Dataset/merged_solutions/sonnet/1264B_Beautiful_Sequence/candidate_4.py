import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    return [int(data[i]) for i in range(4)]


# --- clause: try_start :: (counts: list[int], start: int) -> list[int] ---
def try_start(counts, start):
    left = counts[:]
    if not left[start]:
        return None
    left[start] -= 1
    made = [start]
    cur = start
    while True:
        if cur > 0 and left[cur - 1] > 0:
            cur -= 1
        elif cur < 3 and left[cur + 1] > 0:
            cur += 1
        else:
            break
        left[cur] -= 1
        made.append(cur)
    if sum(left) == 0:
        return made
    return None


# --- clause: main :: () -> None ---
def main():
    counts = read_input()
    for start in (0, 1, 2, 3):
        made = try_start(counts, start)
        if made is not None:
            sys.stdout.write("YES\n" + " ".join(map(str, made)) + "\n")
            return
    sys.stdout.write("NO\n")


if __name__ == "__main__":
    main()
