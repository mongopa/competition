A, D = map(int, input().split())
print(A * (D + 1) if A > D else (A + 1) * D)