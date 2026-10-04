import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    return data[0], data[1], data[2], data[3]

# Clause compute_answer [Confidence: 1.00]
def compute_answer(v1, v2, t, d):
    distance = 0
    for index in range(t):
        cap_left = v1 + index * d
        cap_right = v2 + (t - 1 - index) * d
        distance += min(cap_left, cap_right)
    return distance

# Clause main [Confidence: 0.80]
def main():
    begin_speed, end_speed, duration, delta = read_input()
    print(compute_answer(begin_speed, end_speed, duration, delta))


if __name__ == "__main__":
    main()

