n, m = map(int, input().split())
ans = [0] * (n + 1)
for _ in range(m):
  a, b = map(int, input().split())
  ans[a] += 1
  ans[b] += 1
for i in ans[1:]:
  print(i)
