L, H = map(int, input().split())
N = int(input())
for i in range(N):
  tmp = int(input())
  if tmp < L:
    print(L - tmp)
  elif L <= tmp <= H:
    print(0)
  else:
    print(-1)