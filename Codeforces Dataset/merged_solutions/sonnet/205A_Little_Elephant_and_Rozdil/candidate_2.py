import sys


# --- clause: read_input :: () -> tuple[int, list[int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    times = list(map(int, data[1:n + 1]))
    return n, times


# --- clause: pick_town :: (n: int, times: list[int]) -> str ---
def pick_town(n, times):
    best = min(times)
    if times.count(best) > 1:
        return "Still Rozdil"
    return str(times.index(best) + 1)


# --- clause: main :: () -> None ---
def main():
    n, times = read_input()
    sys.stdout.write("%s\n" % pick_town(n, times))


if __name__ == "__main__":
    main()
