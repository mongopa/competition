import math
N, D = map(int, input().split())
li = [list(map(int, input().split())) for _ in range(N)]
ans = 0
for i in range(N):
  for j in range(i + 1, N):
    diff = 0
    for k in range(D):
      diff += (li[i][k] - li[j][k]) ** 2
    if math.sqrt(diff).is_integer():
      ans += 1
print(ans)
