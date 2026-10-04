import sys


# --- clause: read_input :: () -> tuple[int, int, int, int] ---
def read_input():
    tokens = sys.stdin.buffer.read().split()
    begin_speed = int(tokens[0])
    end_speed = int(tokens[1])
    duration = int(tokens[2])
    delta = int(tokens[3])
    return begin_speed, end_speed, duration, delta


# --- clause: compute_answer :: (v1: int, v2: int, t: int, d: int) -> int ---
def compute_answer(v1, v2, t, d):
    distance = 0
    for index in range(t):
        cap_left = v1 + index * d
        cap_right = v2 + (t - 1 - index) * d
        distance += min(cap_left, cap_right)
    return distance


# --- clause: main :: () -> None ---
def main():
    begin_speed, end_speed, duration, delta = read_input()
    print(compute_answer(begin_speed, end_speed, duration, delta))


if __name__ == "__main__":
    main()
