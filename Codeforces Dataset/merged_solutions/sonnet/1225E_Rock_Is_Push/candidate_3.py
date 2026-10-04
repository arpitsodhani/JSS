import sys

MOD = 1000000007


# --- clause: read_input :: () -> tuple[int, int, list[bytes]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    m = int(data[1])
    grid = []
    for i in range(n):
        grid.append(data[2 + i])
    return n, m, grid


# --- clause: count_paths :: (n: int, m: int, grid: list[bytes]) -> int ---
def count_paths(n, m, grid):
    if n == 1 and m == 1:
        return 1
    rock = 82
    down_sum = [[0] * (m + 2) for _ in range(n + 2)]
    col_rocks = [0] * (m + 2)
    first_right = [0] * (m + 2)
    first_down = [0] * (m + 2)
    right_sum = [0] * (m + 3)
    for i in range(n, 0, -1):
        row = grid[i - 1]
        for j in range(1, m + 1):
            if i == n and j == m:
                first_down[j] = 1
                continue
            reach = n - col_rocks[j]
            if reach >= i + 1:
                first_down[j] = (down_sum[i + 1][j] - down_sum[reach + 1][j]) % MOD
            else:
                first_down[j] = 0
        right_sum[m + 1] = 0
        for j in range(m, 0, -1):
            right_sum[j] = (right_sum[j + 1] + first_down[j]) % MOD
        row_rocks = 0
        j = m
        while j > 0:
            if i == n and j == m:
                first_right[j] = 1
            else:
                reach = m - row_rocks
                if reach >= j + 1:
                    first_right[j] = (right_sum[j + 1] - right_sum[reach + 1]) % MOD
                else:
                    first_right[j] = 0
            if row[j - 1] == rock:
                row_rocks += 1
            j -= 1
        target = down_sum[i]
        source = down_sum[i + 1]
        for j in range(1, m + 1):
            target[j] = (source[j] + first_right[j]) % MOD
        for j in range(1, m + 1):
            if row[j - 1] == rock:
                col_rocks[j] += 1
    return (first_right[1] + first_down[1]) % MOD


# --- clause: main :: () -> None ---
def main():
    n, m, grid = read_input()
    print(count_paths(n, m, grid))


if __name__ == "__main__":
    main()
