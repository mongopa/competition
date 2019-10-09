A, B, C, K = map(int, input().split())
S, T = map(int, input().split())
ALL_MEM = S + T
if ALL_MEM >= K:
  print(S * A + T * B - ALL_MEM * C)
else:
  print(S * A + T * B)