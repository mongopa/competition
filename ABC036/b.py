N = int(input())
li = list(input() for _ in range(N))
ans = [''] * N
for i in range(N):
  for j in range(N):
    ans[i] = li[j][i] + ans[i]
  print(ans[i])