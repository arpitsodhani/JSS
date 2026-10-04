import sys

MOD = 10 ** 9 + 7


# --- clause: read_input :: () -> tuple[int, list[int]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    return n, data[1:1 + n]


# --- clause: total_scalar :: (n: int, a: list[int]) -> int ---
def total_scalar(n, a):
    order = sorted(range(n), key=a.__getitem__)
    left = [0] * (n + 2)
    right = [0] * (n + 2)
    answer = 0
    for index in order:
        pos = index + 1
        mirror = n - pos + 1
        gathered = pos * mirror
        node = pos - 1
        acc = 0
        while node:
            acc += left[node]
            node &= node - 1
        gathered += mirror * acc
        node = n - pos
        acc = 0
        while node:
            acc += right[node]
            node &= node - 1
        gathered += pos * acc
        answer = (answer + a[index] * gathered) % MOD
        node = pos
        while node <= n:
            left[node] += pos
            node += node & -node
        node = mirror
        while node <= n:
            right[node] += mirror
            node += node & -node
    return answer % MOD


# --- clause: main :: () -> None ---
def main():
    n, a = read_input()
    sys.stdout.write(str(total_scalar(n, a)) + "\n")


if __name__ == "__main__":
    main()
