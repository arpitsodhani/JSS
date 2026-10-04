import sys


# --- clause: read_input :: () -> int ---
def read_input():
    return int(sys.stdin.buffer.read().split()[0])

# --- clause: split_candies :: (n: int) -> list[int] ---
def split_candies(n):
    count = int(((8 * n + 1) ** 0.5 - 1) // 2)
    while (count + 1) * (count + 2) // 2 <= n:
        count += 1
    while count * (count + 1) // 2 > n:
        count -= 1
    gifts = [i for i in range(1, count + 1)]
    gifts[count - 1] += n - count * (count + 1) // 2
    return gifts

# --- clause: main :: () -> None ---
def main():
    n = read_input()
    gifts = split_candies(n)
    sys.stdout.write(str(len(gifts)) + "\n" + " ".join(map(str, gifts)) + "\n")


if __name__ == "__main__":
    main()
