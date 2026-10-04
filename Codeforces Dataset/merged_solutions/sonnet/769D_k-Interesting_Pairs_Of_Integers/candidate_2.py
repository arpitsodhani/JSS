# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n, k = data[0], data[1]
    values = data[2:2 + n]
    bits = 14
    limit = 1 << bits

    if k > bits:
        sys.stdout.write("0")
        return

    freq = [0] * limit
    for value in values:
        freq[value] += 1

    if k == 0:
        total = sum(count * (count - 1) // 2 for count in freq)
        sys.stdout.write(str(total))
        return

    answer = 0
    for mask in range(limit):
        if mask.bit_count() == k:
            for value, count in enumerate(freq):
                if count:
                    answer += count * freq[value ^ mask]

    sys.stdout.write(str(answer // 2))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
