import sys


# --- clause: read_input :: () -> tuple[int, int, int, int] ---
def read_input():
    nums = list(map(int, sys.stdin.buffer.read().split()))
    start, finish = nums[0], nums[1]
    seconds, step = nums[2], nums[3]
    return start, finish, seconds, step


# --- clause: compute_answer :: (v1: int, v2: int, t: int, d: int) -> int ---
def compute_answer(v1, v2, t, d):
    answer = 0
    for k in range(t):
        forward = v1 + d * k
        backward = v2 + d * (t - 1 - k)
        answer += forward if forward < backward else backward
    return answer


# --- clause: main :: () -> None ---
def main():
    start, finish, seconds, step = read_input()
    sys.stdout.write(str(compute_answer(start, finish, seconds, step)) + "\n")


if __name__ == "__main__":
    main()
