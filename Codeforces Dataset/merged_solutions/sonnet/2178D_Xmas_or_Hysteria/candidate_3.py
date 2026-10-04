# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def attacks_zero(sorted_elves, n):
    strongest_value, strongest_id = sorted_elves[-1]
    total = 0
    pivot = -1

    for pos in range(n - 2, -1, -1):
        total += sorted_elves[pos][0]
        if total >= strongest_value:
            pivot = pos
            break

    if pivot < 0:
        return None

    result = [(sorted_elves[i + 1][1], sorted_elves[i][1]) for i in range(pivot)]
    result.append((strongest_id, sorted_elves[pivot][1]))
    result.extend((sorted_elves[i][1], strongest_id) for i in range(pivot + 1, n - 1))
    return result

def attacks_positive(sorted_elves, n, m):
    if m > n // 2:
        return None
    return [(sorted_elves[i + m][1], sorted_elves[i][1]) for i in range(n - m)]

def main():
    nums = iter(map(int, sys.stdin.buffer.read().split()))
    tests = next(nums)
    lines = []

    for _ in range(tests):
        n = next(nums)
        m = next(nums)
        sorted_elves = sorted((next(nums), i) for i in range(1, n + 1))

        if n == 1:
            lines.append("0" if m == 1 else "-1")
        elif m == 0:
            ops = attacks_zero(sorted_elves, n)
            if ops is None:
                lines.append("-1")
            else:
                lines.append(str(len(ops)))
                lines.extend(f"{x} {y}" for x, y in ops)
        else:
            ops = attacks_positive(sorted_elves, n, m)
            if ops is None:
                lines.append("-1")
            else:
                lines.append(str(len(ops)))
                lines.extend(f"{x} {y}" for x, y in ops)

# CLAUSE: finish_program
    print("\n".join(lines))

if __name__ == "__main__":
    main()
