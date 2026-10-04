# Clause setup_environment [Confidence: 0.80]
import sys


# Clause solve_logic [Confidence: 1.00]
def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n = data[0]
    counts = [value.bit_count() for value in data[1:1 + n]]

    seen = [1, 0]
    parity = 0
    total_good_parity = 0

    for count in counts:
        parity ^= count & 1
        total_good_parity += seen[parity]
        seen[parity] += 1

    invalid = 0
    for left in range(n):
        segment_sum = 0
        segment_max = 0
        right_limit = min(n, left + 130)
        for right in range(left, right_limit):
            current = counts[right]
            segment_sum += current
            if current > segment_max:
                segment_max = current
            if segment_sum % 2 == 0 and segment_max * 2 > segment_sum:
                invalid += 1

    sys.stdout.write(str(total_good_parity - invalid))


# Clause finish_program [Confidence: 0.60]
if __name__ == "__main__":
    main()


