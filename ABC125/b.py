n = int(input())
vl = list(map(int, input().split()))
cl = list(map(int, input().split()))
ans = 0
for i in range(n):
  dif = vl[i] - cl[i]
  if dif > 0:
    ans += dif
print(ans)