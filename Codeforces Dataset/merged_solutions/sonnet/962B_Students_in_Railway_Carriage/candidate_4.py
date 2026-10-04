import sys


# --- clause: read_input :: () -> tuple[int, int, int, bytes] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    values = list(map(int, data[:3]))
    n, a, b = values[0], values[1], values[2]
    return n, a, b, data[3]


# --- clause: seat_students :: (n: int, a: int, b: int, seats: bytes) -> int ---
def seat_students(n, a, b, seats):
    total = 0
    run = 0
    for i in range(n + 1):
        if i < n and seats[i] == 46:
            run += 1
            continue
        if run:
            small = run // 2
            big = run - small
            if a >= b:
                take_a = a if a < big else big
                take_b = b if b < small else small
            else:
                take_b = b if b < big else big
                take_a = a if a < small else small
            a -= take_a
            b -= take_b
            total += take_a + take_b
            run = 0
    return total


# --- clause: main :: () -> None ---
def main():
    n, a, b, seats = read_input()
    answer = seat_students(n, a, b, seats)
    sys.stdout.write(str(answer) + "\n")


if __name__ == "__main__":
    main()
