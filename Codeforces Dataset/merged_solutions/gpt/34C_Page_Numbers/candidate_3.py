# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _run_case_program():
    import sys

    s = sys.stdin.readline().strip()
    nums = sorted(set(map(int, s.split(','))))

    res = []
    start = prev = nums[0]

    for x in nums[1:]:
        if x == prev + 1:
            prev = x
        else:
            if start == prev:
                res.append(str(start))
            else:
                res.append(f"{start}-{prev}")
            start = prev = x

    if start == prev:
        res.append(str(start))
    else:
        res.append(f"{start}-{prev}")

    print(",".join(res))

# CLAUSE: finish_program
if __name__ == "__main__":
    _run_case_program()
