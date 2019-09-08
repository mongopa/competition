N, Q = map(int, input().split())
li = [0] * N
for i in range(Q):
  L, R, T = map(int, input().split())
  for j in range(L - 1, R):
    li[j] = T

for i in range(N):
  print(li[i])