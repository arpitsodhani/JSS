# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    n, r1, r2, r3, d = numbers[0], numbers[1], numbers[2], numbers[3], numbers[4]
    stages = numbers[5:5 + n]

    stage_costs = [
        (
            min(stage * r1 + r3, (stage + 2) * r1),
            min((stage + 1) * r1, r2),
        )
        for stage in stages
    ]

    resolved = 0
    unfinished = 10 ** 30

    for complete, partial in stage_costs[:-1]:
        keep_resolved = resolved + complete + d
        close_unfinished = unfinished + complete + 2 * d
        make_unfinished = resolved + partial + 2 * d
        continue_unfinished = unfinished + partial + 2 * d
        resolved = keep_resolved if keep_resolved < close_unfinished else close_unfinished
        unfinished = make_unfinished if make_unfinished < continue_unfinished else continue_unfinished

    complete, partial = stage_costs[-1]
    candidates = (
        resolved + complete,
        unfinished + complete + d,
        resolved + partial + r1,
        unfinished + partial + r1 + d,
    )
    sys.stdout.write(str(min(candidates)))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
