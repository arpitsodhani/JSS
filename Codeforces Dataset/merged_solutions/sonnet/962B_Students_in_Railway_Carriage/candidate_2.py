import sys


# --- clause: read_input :: () -> tuple[int, int, int, bytes] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    a = int(data[1])
    b = int(data[2])
    n, a, b = int(data[0]), int(data[1]), int(data[2])
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
            big = (run + 1) // 2
            small = run // 2
            if a < b:
                take_b = min(b, big)
                take_a = min(a, small)
            else:
                take_a = min(a, big)
                take_b = min(b, small)
            a -= take_a
            b -= take_b
            total += take_a + take_b
            run = 0
    return total


# --- clause: main :: () -> None ---
def main():
    n, a, b, seats = read_input()
    sys.stdout.write("%d\n" % seat_students(n, a, b, seats))


if __name__ == "__main__":
    main()
