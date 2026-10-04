# CLAUSE: setup_environment
import sys

def main():
    nums = list(map(int, sys.stdin.buffer.read().split()))
    q = nums[0]
    at = 1
    res = []

# CLAUSE: solve_logic
    for _ in range(q):
        n = nums[at]
        k = nums[at + 1]
        at += 2

        arr = nums[at:at + n]
        at += n

        marks = nums[at:at + k]
        at += k
        marks.sort()

        target = arr[marks[0] - 1]
        edge_counts = [0] * (k + 1)
        mark_ptr = 0
        previous = 0
        transitions = 0

        for boundary in range(1, n + 2):
            while mark_ptr < k and marks[mark_ptr] < boundary:
                mark_ptr += 1

            current = 0
            if boundary <= n:
                current = arr[boundary - 1] ^ target

            if current != previous:
                edge_counts[mark_ptr] += 1
                transitions += 1

            previous = current

        best_local = 0
        for value in edge_counts:
            if value > best_local:
                best_local = value

        runs = transitions // 2
        res.append(str(runs if runs > best_local else best_local))

# CLAUSE: finish_program
    print("\n".join(res))

if __name__ == "__main__":
    main()
