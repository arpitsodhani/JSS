import sys

MOD = 10**9 + 7

def main():
    data = sys.stdin.read().strip().split()
    t = int(data[0])
    idx = 1
    out = []
    for _ in range(t):
        x = int(data[idx])
        s = data[idx + 1]
        idx += 2

        arr = list(s)
        length = len(arr)

        for i in range(x):
            d = ord(arr[i]) - 48
            length = (length + (length - i - 1) * (d - 1)) % MOD

            if len(arr) < x:
                suffix = arr[i + 1:]
                need = x - len(arr)
                for _ in range(d - 1):
                    if need <= 0:
                        break
                    take = min(need, len(suffix))
                    arr.extend(suffix[:take])
                    need -= take

        out.append(str(length % MOD))

    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()
