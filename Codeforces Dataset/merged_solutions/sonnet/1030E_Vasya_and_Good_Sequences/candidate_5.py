# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def read_counts():
    data = sys.stdin.buffer.read().split()
    if not data:
        return []
    size = int(data[0])
    return [int(token).bit_count() for token in data[1:size + 1]]

def main():
    counts = read_counts()
    n = len(counts)
    if n == 0:
        return

    prefix_even = 1
    prefix_odd = 0
    running = 0
    answer = 0

    for value in counts:
        running ^= value & 1
        if running:
            answer += prefix_odd
            prefix_odd += 1
        else:
            answer += prefix_even
            prefix_even += 1

    rejected = 0
    for left in range(n):
        total = 0
        biggest = 0
        for value in counts[left:left + 130]:
            total += value
            biggest = max(biggest, value)
            rejected += int((total & 1) == 0 and biggest + biggest > total)

    print(answer - rejected)

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
