import sys


# --- clause: read_input :: () -> list[tuple[int, str]] ---
def read_input():
    fields = sys.stdin.buffer.read().split()
    t = int(fields[0])
    cursor = 1
    cases = []
    for _ in range(t):
        k = int(fields[cursor + 1])
        s = fields[cursor + 2].decode()
        cursor += 3
        cases.append((k, s))
    return cases


# --- clause: matched_flags :: (s: str, gone: list[int]) -> list[int] ---
def matched_flags(s, gone):
    n = len(s)
    matched = [0] * n
    stack = []
    for i in range(n):
        if gone[i]:
            continue
        if s[i] == "(":
            stack.append(i)
        elif stack:
            matched[stack.pop()] = 1
            matched[i] = 1
    return matched


# --- clause: plan_removals :: (k: int, s: str) -> list[int] ---
def plan_removals(k, s):
    n = len(s)
    gone = [0] * n
    for _ in range(k):
        matched = matched_flags(s, gone)
        last_close = -1
        first_open = -1
        for i in range(n):
            if gone[i] or not matched[i]:
                continue
            if s[i] == ")":
                last_close = i
            elif first_open < 0:
                first_open = i
        if last_close < 0:
            break
        loose = False
        for i in range(last_close + 1, n):
            if not gone[i] and not matched[i] and s[i] == ")":
                loose = True
                break
        gone[last_close if not loose else first_open] = 1
    return gone


# --- clause: main :: () -> None ---
def main():
    collected = []
    for k, s in read_input():
        collected.append("".join(map(str, plan_removals(k, s))))
    sys.stdout.write("\n".join(collected) + "\n")


if __name__ == "__main__":
    main()
