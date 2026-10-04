# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
class RunStack:
    def __init__(self):
        self.data = []

    def add(self, value, duration):
        self.data.append([value, duration])
        while self.reduce_once():
            continue
        return self.data[-1][1]

    def reduce_once(self):
        data = self.data
        if len(data) >= 2 and data[-1][0] == data[-2][0]:
            data[-2][1] += data[-1][1]
            data.pop()
            return True
        if len(data) >= 3 and data[-1][0] == data[-3][0]:
            left_duration = data[-3][1]
            middle_duration = data[-2][1]
            right_duration = data[-1][1]
            if middle_duration < left_duration and middle_duration < right_duration:
                value = data[-1][0]
                duration = left_duration + right_duration - middle_duration
                del data[-3:]
                data.append([value, duration])
                return True
        return False

def main():
    raw = sys.stdin.buffer.read().split()
    idx = 0
    cases = int(raw[idx])
    idx += 1
    rows = []
    for _ in range(cases):
        n = int(raw[idx])
        idx += 1
        stack = RunStack()
        best = 0
        row = []
        for _ in range(n):
            duration = int(raw[idx])
            value = int(raw[idx + 1])
            idx += 2
            last = stack.add(value, duration)
            if last > best:
                best = last
            row.append(str(best))
        rows.append(" ".join(row))
    sys.stdout.write("\n".join(rows))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
