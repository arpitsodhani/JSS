n, k = map(int, input().split())

diplomas = (n // 2) // (k + 1)
certificates = diplomas * k
others = n - diplomas - certificates

print(diplomas, certificates, others)
