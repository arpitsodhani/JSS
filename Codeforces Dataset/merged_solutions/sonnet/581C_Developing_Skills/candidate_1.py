import sys


# --- clause: read_input :: () -> tuple[int, int, list[int]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    k = data[1]
    return n, k, data[2:2 + n]


# --- clause: best_rating :: (n: int, k: int, skills: list[int]) -> int ---
def best_rating(n, k, skills):
    rating = 0
    steps = []
    for value in skills:
        rating += value // 10
        if value % 10:
            steps.append(10 - value % 10)
    steps.sort()
    for cost in steps:
        if k < cost:
            break
        k -= cost
        rating += 1
    room = 10 * n - rating
    extra = k // 10
    if extra > room:
        extra = room
    return rating + extra


# --- clause: main :: () -> None ---
def main():
    n, k, skills = read_input()
    sys.stdout.write(str(best_rating(n, k, skills)) + "\n")


if __name__ == "__main__":
    main()
