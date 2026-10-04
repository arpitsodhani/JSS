import sys


# --- clause: read_input :: () -> list[list[int]] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    t = numbers[0]
    cursor = 1
    cases = []
    for _ in range(t):
        n = numbers[cursor]
        cursor += 1
        cases.append(numbers[cursor:cursor + n])
        cursor += n
    return cases


# --- clause: happy_widths :: (a: list[int]) -> str ---
def happy_widths(a):
    n = len(a)
    good = ["0"] * (n + 1)
    low = 2
    high = n + 1
    while low < high:
        k = (low + high) // 2
        window = []
        head = 0
        seen = [0] * (n + 2)
        fine = True
        for i in range(n):
            while len(window) > head and a[window[-1]] >= a[i]:
                window.pop()
            window.append(i)
            if window[head] <= i - k:
                head += 1
            if i >= k - 1:
                value = a[window[head]]
                if value > n - k + 1 or seen[value]:
                    fine = False
                    break
                seen[value] = 1
        if fine:
            high = k
        else:
            low = k + 1
    for k in range(low, n + 1):
        good[k] = "1"
    seen = [0] * (n + 2)
    single = True
    for value in a:
        if value > n or seen[value]:
            single = False
            break
        seen[value] = 1
    good[1] = "1" if single else "0"
    return "".join(good[1:])


# --- clause: main :: () -> None ---
def main():
    out = []
    for a in read_input():
        out.append(happy_widths(a))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
