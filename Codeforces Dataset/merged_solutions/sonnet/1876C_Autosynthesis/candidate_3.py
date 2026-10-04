import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    fields = list(map(int, sys.stdin.buffer.read().split()))
    return fields[1:1 + fields[0]]


# --- clause: choose_circled :: (a: list[int]) -> list[int] | None ---
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
    front = 0
    while front < len(queue):
        v = queue[front]
        front += 1
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
        spot_id = v
        while state[spot_id] == 0:
            state[spot_id] = 1 if len(walk) % 2 == 0 else 2
            walk.append(spot_id)
            spot_id = a[spot_id - 1]
        if len(walk) % 2:
            return None
    return state


# --- clause: main :: () -> None ---
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
