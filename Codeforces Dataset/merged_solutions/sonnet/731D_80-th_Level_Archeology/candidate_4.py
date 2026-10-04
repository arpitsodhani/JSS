# CLAUSE: setup_environment
import sys

def add_segment(events, left, right):
    if left <= right:
        events.append((left, 1))
        events.append((right + 1, -1))

# CLAUSE: solve_logic
def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n, c = data[0], data[1]
    at = 2
    last = []
    events = []

    for i in range(n):
        ln = data[at]
        at += 1
        word = data[at:at + ln]
        at += ln

        if i:
            j = 0
            cap = min(len(last), len(word))
            while j < cap and last[j] == word[j]:
                j += 1
            if j == cap:
                if len(last) > len(word):
                    sys.stdout.write("-1")
                    return
            else:
                a = last[j] - 1
                b = word[j] - 1
                if a < b:
                    add_segment(events, c - b, c - a - 1)
                else:
                    add_segment(events, 0, c - a - 1)
                    add_segment(events, c - b, c - 1)

        last = word

    events.sort()
    active = 0
    position = 0
    idx = 0
    total = len(events)

    while idx < total:
        point = events[idx][0]
        if position < point and active == 0:
            sys.stdout.write(str(position))
            return
        while idx < total and events[idx][0] == point:
            active += events[idx][1]
            idx += 1
        position = point
        if position < c and active == 0:
            sys.stdout.write(str(position))
            return

    if position < c and active == 0:
        sys.stdout.write(str(position))
    else:
        sys.stdout.write("-1")

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
