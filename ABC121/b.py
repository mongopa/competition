N, M, C = map(int, input().split())
bl = list(map(int, input().split()))
ans = 0
for i in range(N):
  l = list(map(int, input().split()))
  tmp = 0
  for j in range(M):
    tmp += bl[j] * l[j]
  if tmp + C > 0:
    ans += 1
print(ans)