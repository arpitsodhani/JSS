# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def prime_divisors(value):
    result = []
    candidate = 2
    while candidate * candidate <= value:
        if value % candidate == 0:
            result.append(candidate)
            while value % candidate == 0:
                value //= candidate
        candidate += 1
    if value > 1:
        result.append(value)
    return result

def movement_needed(pos, block):
    answer = 0
    start = 0
    while start < len(pos):
        center = pos[start + block // 2]
        end = start + block
        idx = start
        while idx < end:
            if pos[idx] >= center:
                answer += pos[idx] - center
            else:
                answer += center - pos[idx]
            idx += 1
        start = end
    return answer

def main():
    tokens = sys.stdin.buffer.read().split()
    n = int(tokens[0])
    ones = [i for i, value in enumerate(tokens[1:n + 1]) if value == b"1"]
    amount = len(ones)

    if amount < 2:
        print(-1)
        return

    best = None
    for divisor in prime_divisors(amount):
        current = movement_needed(ones, divisor)
        if best is None or current < best:
            best = current

    print(best)

# CLAUSE: finish_program
main()
