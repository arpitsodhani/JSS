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
    partial = []
    for value in skills:
        rating += value // 10
        if value % 10:
            partial.append(10 - value % 10)
    for cost in sorted(partial):
        if k >= cost:
            k -= cost
            rating += 1
        else:
            break
    limit = 10 * n
    while k >= 10 and rating < limit:
        k -= 10
        rating += 1
    return rating


# --- clause: main :: () -> None ---
def main():
    n, k, skills = read_input()
    sys.stdout.write(str(best_rating(n, k, skills)) + "\n")


if __name__ == "__main__":
    main()
