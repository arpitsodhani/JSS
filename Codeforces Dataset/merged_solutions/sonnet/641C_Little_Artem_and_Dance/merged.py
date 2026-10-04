import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    q = data[1]
    return n, q, data[2:]

# Clause final_offsets [Confidence: 1.00]
def final_offsets(n, q, moves):
    odd = 0
    even = 0
    pos = 0
    for _ in range(q):
        kind = moves[pos]
        pos += 1
        if kind == 1:
            shift = moves[pos]
            pos += 1
            odd = (odd + shift) % n
            even = (even + shift) % n
        else:
            if odd % 2 == 0:
                odd = (odd + 1) % n
                even = (even - 1) % n
            else:
                odd = (odd - 1) % n
                even = (even + 1) % n
    return odd, even

# Clause arrange [Confidence: 1.00]
def arrange(n, odd, even):
    result = [0] * n
    for boy in range(1, n + 1):
        shift = odd if boy % 2 else even
        girl = (boy - 1 + shift) % n
        result[girl] = boy
    return result

# Clause main [Confidence: 1.00]
def main():
    n, q, moves = read_input()
    odd, even = final_offsets(n, q, moves)
    sys.stdout.write(" ".join(map(str, arrange(n, odd, even))) + "\n")


if __name__ == "__main__":
    main()

