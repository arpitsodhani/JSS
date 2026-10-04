import sys


# --- clause: read_input :: () -> tuple[int, list[bytes], list[int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    lists = list(data[1:1 + n])
    guess = [int(token) for token in data[1 + n:1 + 2 * n]]
    return n, lists, guess


# --- clause: pick_guests :: (n: int, lists: list[bytes], guess: list[int]) -> list[int] ---
def pick_guests(n, lists, guess):
    need = list(guess)
    coming = []
    invited = [False] * n
    queue = [i for i in range(n) if need[i] == 0]
    while queue:
        i = queue.pop()
        if invited[i]:
            continue
        invited[i] = True
        coming.append(i + 1)
        row = lists[i]
        for j in range(n):
            if row[j] == 49:
                need[j] -= 1
                if need[j] == 0 and not invited[j]:
                    queue.append(j)
    return coming


# --- clause: main :: () -> None ---
def main():
    n, lists, guess = read_input()
    coming = pick_guests(n, lists, guess)
    sys.stdout.write("%d\n%s\n" % (len(coming), " ".join(map(str, coming))))


if __name__ == "__main__":
    main()
