# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def maximum_subarray(values):
    running = 0
    answer = None
    for number in values:
        running += number
        if answer is None or running > answer:
            answer = running
        if running < 0:
            running = 0
    return answer

def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    index = 1
    result = []
    for _ in range(data[0]):
        length = data[index]
        index += 1
        segment = data[index:index + length]
        index += length
        result.append(str(maximum_subarray(segment)))
    print("\n".join(result))

# CLAUSE: finish_program
solve()
