# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _run_case_program():
    import sys

    data = list(map(float, sys.stdin.read().split()))
    vp, vd, t, f, c = data

    if vp >= vd:
        print(0)
    else:
        pos = vp * t
        ans = 0

        while pos < c:
            catch_time = pos / (vd - vp)
            catch_pos = pos + vp * catch_time

            if catch_pos >= c:
                break

            ans += 1
            return_time = catch_pos / vd
            pos = catch_pos + vp * (return_time + f)

        print(ans)

# CLAUSE: finish_program
if __name__ == "__main__":
    _run_case_program()
