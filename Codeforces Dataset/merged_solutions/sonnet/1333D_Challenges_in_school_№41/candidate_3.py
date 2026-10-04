# CLAUSE: setup_environment
import sys
from collections import deque

def collect_layers(n, chars):
    layers = []
    move_count = 0
    changed = True
    while changed:
        changed = False
        layer = deque()
        i = 0
        while i < n - 1:
            pair = chars[i] + chars[i + 1]
            if pair == "RL":
                layer.append(i + 1)
                chars[i] = "L"
                chars[i + 1] = "R"
                changed = True
                i += 2
            else:
                i += 1
        if changed:
            layers.append(layer)
            move_count += len(layer)
    return layers, move_count

# CLAUSE: solve_logic
def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    k = int(data[1])
    chars = list(data[2].decode())

    layers, move_count = collect_layers(n, chars)
    required = len(layers)

    if k < required or k > move_count:
        print(-1)
        return

    need_extra = k - required
    result = []

    for layer in layers:
        while need_extra and len(layer) > 1:
            result.append([layer.popleft()])
            need_extra -= 1
        result.append(list(layer))

# CLAUSE: finish_program
    sys.stdout.write("\n".join(
        "{} {}".format(len(group), " ".join(str(x) for x in group))
        for group in result
    ))

if __name__ == "__main__":
    main()
