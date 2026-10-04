import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    return numbers[1:1 + numbers[0]]


# --- clause: choose_circled :: (a: list[int]) -> list[int] | None ---
def choose_circled(a):
    n = len(a)
    state = [0] * (n + 1)
    incoming = [[] for _ in range(n + 1)]
    for i in range(1, n + 1):
        incoming[a[i - 1]].append(i)
    stack = []
    for v in range(1, n + 1):
        if not incoming[v]:
            stack.append(v)
    left = [len(incoming[v]) for v in range(n + 1)]
    while stack:
        v = stack.pop()
        if state[v]:
            continue
        state[v] = 1
        target = a[v - 1]
        if state[target] == 1:
            return None
        if state[target] == 0:
            state[target] = 2
            beyond = a[target - 1]
            left[beyond] -= 1
            if left[beyond] == 0 and state[beyond] == 0:
                stack.append(beyond)
    for v in range(1, n + 1):
        if state[v]:
            continue
        node = v
        step = 0
        while state[node] == 0:
            state[node] = 1 if step % 2 == 0 else 2
            step += 1
            node = a[node - 1]
        if step % 2:
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
