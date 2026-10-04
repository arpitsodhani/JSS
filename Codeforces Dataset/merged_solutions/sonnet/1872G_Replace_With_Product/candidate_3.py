# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def choose_segment(a):
    n = len(a)
    pref = [0]
    heavy = []
    for i in range(n):
        pref.append(pref[-1] + a[i])
        if a[i] != 1:
            heavy.append(i)

    if len(heavy) == 0:
        return 1, 1

    if len(heavy) > 70:
        return heavy[0] + 1, heavy[-1] + 1

    best_gain = 0
    answer_l = 0
    answer_r = 0
    start = 0
    while start < len(heavy):
        product = 1
        end = start
        while end < len(heavy):
            product *= a[heavy[end]]
            l = heavy[start]
            r = heavy[end]
            segment_sum = pref[r + 1] - pref[l]
            improvement = product - segment_sum
            if improvement > best_gain:
                best_gain = improvement
                answer_l = l
                answer_r = r
            end += 1
        start += 1

    return answer_l + 1, answer_r + 1

def main():
    values = list(map(int, sys.stdin.buffer.read().split()))
    at = 1
    results = []
    for _ in range(values[0]):
        n = values[at]
        at += 1
        arr = values[at:at + n]
        at += n
        l, r = choose_segment(arr)
        results.append(f"{l} {r}")
    print("\n".join(results))

# CLAUSE: finish_program
main()
