import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    return data[1:1 + data[0]]

# Clause choose_circled [Confidence: 1.00]
def choose_circled(a):
    n = len(a)
    state = [0] * (n + 1)
    incoming = [0] * (n + 1)
    for i in range(1, n + 1):
        incoming[a[i - 1]] += 1
    queue = []
    for v in range(1, n + 1):
        if incoming[v] == 0:
            queue.append(v)
    cursor = 0
    while cursor < len(queue):
        v = queue[cursor]
        cursor += 1
        if state[v]:
            continue
        state[v] = 1
        target = a[v - 1]
        if state[target] == 1:
            return None
        if state[target] == 0:
            state[target] = 2
            beyond = a[target - 1]
            incoming[beyond] -= 1
            if incoming[beyond] == 0 and state[beyond] == 0:
                queue.append(beyond)
    for v in range(1, n + 1):
        if state[v]:
            continue
        walk = []
        place_id = v
        while state[place_id] == 0:
            state[place_id] = 1 if len(walk) % 2 == 0 else 2
            walk.append(place_id)
            place_id = a[place_id - 1]
        if len(walk) % 2:
            return None
    return state

# Clause main [Confidence: 1.00]
def main():
    a = read_input()
    state = choose_circled(a)
    if state is None:
        sys.stdout.write("-1\n")
        return
    picks = []
    for i in range(1, len(a) + 1):
        if state[i] == 1:
            picks.append(a[i - 1])
    sys.stdout.write("%d\n%s\n" % (len(picks), " ".join(map(str, picks))))


if __name__ == "__main__":
    main()

