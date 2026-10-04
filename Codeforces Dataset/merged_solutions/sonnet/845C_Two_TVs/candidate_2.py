# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n = data[0]
    events = []
    pos = 1
    for _ in range(n):
        l = data[pos]
        r = data[pos + 1]
        pos += 2
        events.append((l, 1))
        events.append((r, -1))
    events.sort(key=lambda item: (item[0], -item[1]))
    active = 0
    answer = "YES"
    for _, delta in events:
        active += delta
        if active > 2:
            answer = "NO"
            break
    sys.stdout.write(answer)

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
