import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    a = int(data[1])
    b = int(data[2])
    return n, a, b, data[3]

# Clause seat_students [Confidence: 1.00]
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

# Clause main [Confidence: 1.00]
def main():
    n, a, b, seats = read_input()
    sys.stdout.write(str(seat_students(n, a, b, seats)) + "\n")


if __name__ == "__main__":
    main()

