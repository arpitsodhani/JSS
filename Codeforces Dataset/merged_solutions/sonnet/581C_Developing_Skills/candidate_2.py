import sys


# --- clause: read_input :: () -> tuple[int, int, list[int]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    k = data[1]
    return n, k, data[2:2 + n]


# --- clause: best_rating :: (n: int, k: int, skills: list[int]) -> int ---
def best_rating(n, k, skills):
    rating = sum(value // 10 for value in skills)
    buckets = [0] * 11
    for value in skills:
        rest = value % 10
        if rest:
            buckets[10 - rest] += 1
    for cost in range(1, 11):
        count = buckets[cost]
        if not count:
            continue
        afford = k // cost
        if afford > count:
            afford = count
        rating += afford
        k -= afford * cost
    room = 10 * n - rating
    extra = k // 10
    return rating + (extra if extra < room else room)


# --- clause: main :: () -> None ---
def main():
    n, k, skills = read_input()
    sys.stdout.write(str(best_rating(n, k, skills)) + "\n")


if __name__ == "__main__":
    main()
