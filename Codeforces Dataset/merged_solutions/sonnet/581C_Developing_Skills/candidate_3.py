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
    costs = []
    for value in skills:
        rating += value // 10
        remainder = value % 10
        if remainder != 0:
            costs.append(10 - remainder)
    costs.sort()
    index = 0
    while index < len(costs) and k >= costs[index]:
        k -= costs[index]
        rating += 1
        index += 1
    headroom = 10 * n - rating
    bonus = k // 10
    if bonus > headroom:
        bonus = headroom
    return rating + bonus


# --- clause: main :: () -> None ---
def main():
    n, k, skills = read_input()
    sys.stdout.write(str(best_rating(n, k, skills)) + "\n")


if __name__ == "__main__":
    main()
