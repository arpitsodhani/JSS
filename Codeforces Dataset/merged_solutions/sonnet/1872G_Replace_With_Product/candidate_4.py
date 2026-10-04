# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    nums = list(map(int, sys.stdin.buffer.read().split()))
    q = nums[0]
    ptr = 1
    lines = []

    for _ in range(q):
        n = nums[ptr]
        ptr += 1
        arr = nums[ptr:ptr + n]
        ptr += n

        prefix = [0]
        useful = []
        running = 0
        for index, value in enumerate(arr):
            running += value
            prefix.append(running)
            if value > 1:
                useful.append((index, value))

        count = len(useful)
        if count == 0:
            lines.append("1 1")
            continue

        if count > 70:
            lines.append(f"{useful[0][0] + 1} {useful[-1][0] + 1}")
            continue

        chosen = (0, 0)
        largest = 0
        for left_index in range(count):
            multiplied = 1
            lpos = useful[left_index][0]
            for right_index in range(left_index, count):
                rpos, val = useful[right_index]
                multiplied *= val
                removed = prefix[rpos + 1] - prefix[lpos]
                delta = multiplied - removed
                if delta > largest:
                    largest = delta
                    chosen = (lpos, rpos)

        lines.append(f"{chosen[0] + 1} {chosen[1] + 1}")

    sys.stdout.write("\n".join(lines))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
