import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    return list(map(int, data[:4]))


# --- clause: try_start :: (counts: list[int], start: int) -> list[int] ---
def try_start(counts, start):
    left = list(counts)
    if left[start] == 0:
        return None
    left[start] -= 1
    made = [start]
    cur = start
    while True:
        if cur and left[cur - 1]:
            cur -= 1
        elif cur != 3 and left[cur + 1]:
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
    for start in range(4):
        made = try_start(counts, start)
        if made is not None:
            sys.stdout.write("YES\n%s\n" % " ".join(map(str, made)))
            return
    sys.stdout.write("NO\n")


if __name__ == "__main__":
    main()
