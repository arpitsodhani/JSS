import sys


def decide(token):
    s = token.strip().lower()
    if s in {"zero", "|0>", "0"}:
        return 0
    if s in {"plus", "|+>", "+", "1"}:
        return 1
    return -1


def main():
    data = sys.stdin.read().split()
    if not data:
        return
    out = [str(decide(x)) for x in data]
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()
