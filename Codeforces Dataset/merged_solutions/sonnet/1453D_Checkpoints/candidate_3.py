import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    fields = list(map(int, sys.stdin.buffer.read().split()))
    return fields[1:1 + fields[0]]


# --- clause: build_stages :: (k: int) -> list[int] | None ---
def build_stages(k):
    if k % 2:
        return None
    stages = []
    begin = k
    while begin > 0:
        length_of = 1
        while (1 << (length_of + 2)) - 2 <= begin:
            length_of += 1
        begin -= (1 << (length_of + 1)) - 2
        stages.append(1)
        for _ in range(length_of - 1):
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
