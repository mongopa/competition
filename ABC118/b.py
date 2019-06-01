n, m = map(int, input().split())
li = []
for i in range(n):
  l = list(map(int,input().split()))
  for j in l[1:]:
    li.append(j)
ans = 0
for i in range(31):
  if li.count(i) == n:
    ans += 1
print(ans)