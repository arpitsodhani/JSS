import sys


# --- clause: read_input :: () -> tuple[int, int, int, bytes] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    a = int(data[1])
    b = int(data[2])
    return n, a, b, bytes(data[3])


# --- clause: seat_students :: (n: int, a: int, b: int, seats: bytes) -> int ---
def seat_students(n, a, b, seats):
    total = 0
    run = 0
    i = 0
    while i <= n:
        if i < n and seats[i] == 46:
            run += 1
            i += 1
            continue
        i += 1
        if run:
            big = (run + 1) // 2
            small = run // 2
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
    print(seat_students(n, a, b, seats))


if __name__ == "__main__":
    main()
