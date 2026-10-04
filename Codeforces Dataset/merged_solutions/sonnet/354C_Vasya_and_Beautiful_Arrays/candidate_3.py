# CLAUSE: setup_environment
import sys

def build_counter(values, size):
    counter = [0] * (size + 1)
    for value in values:
        counter[value] += 1
    return counter

# CLAUSE: solve_logic
def build_prefix(counter):
    pref = counter[:]
    for index in range(1, len(pref)):
        pref[index] += pref[index - 1]
    return pref

def covered_count(step, largest, pref, k):
    total = 0
    multiple = step
    while multiple <= largest:
        end = multiple + k
        next_before = multiple + step - 1
        if end > next_before:
            end = next_before
        if end > largest:
            end = largest
        total += pref[end] - pref[multiple - 1]
        multiple += step
    return total

def main():
    raw = sys.stdin.buffer.read().split()
    n = int(raw[0])
    k = int(raw[1])
    values = [int(x) for x in raw[2:]]
    largest = max(values)
    smallest = min(values)
    pref = build_prefix(build_counter(values, largest))
    answer = 1
    candidate = smallest
    while candidate >= 1:
        if covered_count(candidate, largest, pref, k) == n:
            answer = candidate
            break
        candidate -= 1
    print(answer)

# CLAUSE: finish_program
main()
