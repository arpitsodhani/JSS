import sys


# --- clause: read_input :: () -> tuple[int, list[int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    times = [int(data[i + 1]) for i in range(n)]
    return n, times


# --- clause: pick_town :: (n: int, times: list[int]) -> str ---
def pick_town(n, times):
    best = times[0]
    spot = 0
    count = 1
    for i in range(1, n):
        if times[i] < best:
            best = times[i]
            spot = i
            count = 1
        elif times[i] == best:
            count += 1
    if count == 1:
        return str(spot + 1)
    return "Still Rozdil"


# --- clause: main :: () -> None ---
def main():
    n, times = read_input()
    answer = pick_town(n, times)
    sys.stdout.write(answer + "\n")


if __name__ == "__main__":
    main()
