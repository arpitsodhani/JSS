n, k = map(int, input().split())

if k == n:
    print("1" * n)
else:
    zeros = k - 1
    ones = n - k + 1
    
    result = []
    if ones >= zeros:
        # Alternate starting with 1
        while ones > 0 or zeros > 0:
            if ones > 0:
                result.append("1")
                ones -= 1
            if zeros > 0:
                result.append("0")
                zeros -= 1
    else:
        # Alternate starting with 0
        while zeros > 0 or ones > 0:
            if zeros > 0:
                result.append("0")
                zeros -= 1
            if ones > 0:
                result.append("1")
                ones -= 1
    
    print("".join(result))
