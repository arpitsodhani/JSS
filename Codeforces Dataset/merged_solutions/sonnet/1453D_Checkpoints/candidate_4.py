import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    return numbers[1:1 + numbers[0]]


# --- clause: build_stages :: (k: int) -> list[int] | None ---
def build_stages(k):
    if k % 2:
        return None
    stages = []
    left = k
    size = 11
    while left > 0:
        while (1 << (size + 1)) - 2 > left:
            size -= 1
        left -= (1 << (size + 1)) - 2
        stages.append(1)
        for _ in range(size - 1):
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
