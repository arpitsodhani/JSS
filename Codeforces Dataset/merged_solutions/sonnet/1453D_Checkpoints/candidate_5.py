import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    return raw[1:1 + raw[0]]


# --- clause: build_stages :: (k: int) -> list[int] | None ---
def build_stages(k):
    if k % 2:
        return None
    stages = []
    first_side = k
    while first_side > 0:
        width = 1
        while (1 << (width + 2)) - 2 <= first_side:
            width += 1
        first_side -= (1 << (width + 1)) - 2
        stages.append(1)
        for _ in range(width - 1):
            stages.append(0)
    return stages


# --- clause: main :: () -> None ---
def main():
    out = []
    for k in read_input():
        stages = build_stages(k)
        if stages is None:
            out.append("-1")
        else:
            out.append(str(len(stages)))
            out.append(" ".join(map(str, stages)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
